# Auto-generation

## Quickstart

``` shell
# install the necessary requirements
make requirements
source ./ci/virtualenv/bin/activate

# change to the etc/ directory
cd etc/

# generate actions from the cached API definitions
./generate_actions.py generate -a ./api_definitions_2017_09_15/
```


## Advanced Usage - Fetch API

**Usecase:** Let's say you have a running Foreman server and want to fetch the current API 
defintions from this server.

``` shell
# assuming you have virtualenv activated and are in etc/

# fetch the api definitions
./generate_actions.py fetch-api -s foreman.domain.tld -u admin -p xxx

# find your new api definitions (should be ./api_definitions_YY_MM_DD with today's date)
ls

# generate the api definitions
./generate_actions.py generate -a ./api_definitions_YY_MM_DD/
```


## Advanced Usage - Manually Fetching the API

Under the hood `python-foreman` is simply downloading the JSON data from a running
Foreman instance. Good news is that this isn't terribly special and you can
go grab the data yourself, if you like. The API definition on a running Foreman
instance is available at: `https://<foreman_server>/apidoc/v2.json`


## How does it work

We utilize a package called [python-foreman](https://github.com/david-caro/python-foreman/)
to fetch the API and cache it in our local directory. It then uses this API 
defintion to generate a bunch of python code under the class `foreman.client.Foreman`

In our generate script we do something similar to:

``` python
from foreman.client import Foreman

# ... 

    self.client = Foreman('https://{}/'.format(self.cli_args.server),
                              auth=(self.cli_args.username, self.cli_args.password),
                              api_version=self.api_version,
                              use_cache=False,
                              cache_dir=api_definition)
```

This code instantiates a new client, connects to the server and fetches the API,
saving it in our cache location.

From here we inspect this `client` object for all of its members. Any member of
`client` that is an instance of `foreman.client.Resource` means it's a Foreman
endpoint that was auto-generated from the API defintion (hosts, activation_keys, etc).

The `foreman.client.Resource` object has a member named `_own_methods` that is a
list strings for all of the functions that correspond to actions that can be
performed on that resource/endpoint. 

Each "method" is an object and can be called just like a function from the resource.
However, it also has members and one of those members is called `defs` that represents
the method "defintion". This method defintion object is the key to the puzzle.
It contains all of the information needed to generate the actions such as:

* name        - name of the method
* resource    - endpoint it lives on
* parameters  - list of all arguments this method taks
* url         - URL representation of the method
* description - description of the method
* http method - GET, POST, DELETE, etc

We then gather up all of these method defintions, each one represents an Action
for StackStorm. We iterate over all of the definitions and render the `etc/action.yaml.j2`
Jinja template using information from the defintion as context. The result of this
rendering gets output to a file in the `actions/` directory with the name of the
action as the filename.

We also use the method defintion information to render the `etc/action_table.md.j2`
Jinja template and output a new line to the `etc/action_table.md` file. This file
is used to generate the action table in `README.md` in the root of this repo.

I hope this "high level" description helps others that read through this code
to understand what's going on and potentially help improve it over time.


# Thanks

A huge thank you goes out to [David Caro](https://github.com/david-caro) for
creating a great library that makes it very easy for others to utilize for
code autogeneration!
