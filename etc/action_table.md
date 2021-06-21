| Action | Foreman API | Description |
|--------|-------------|-------------|
| activation_keys.add_host_collections | [POST /katello/api/activation_keys/:id/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/add_host_collections.html)  |  |
| activation_keys.add_subscriptions | [PUT /katello/api/activation_keys/:id/add_subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/add_subscriptions.html)  | Attach a subscription |
| activation_keys.available_host_collections | [GET /katello/api/activation_keys/:id/host_collections/available](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/available_host_collections.html)  | List host collections the activation key does not belong to |
| activation_keys.available_releases | [GET /katello/api/activation_keys/:id/releases](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/available_releases.html)  | Show release versions available for an activation key |
| activation_keys.content_override | [PUT /katello/api/activation_keys/:id/content_override](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/content_override.html)  | Override content for activation_key |
| activation_keys.copy | [POST /katello/api/activation_keys/:id/copy](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/copy.html)  | Copy an activation key |
| activation_keys.create | [POST /katello/api/activation_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/create.html)  | Create an activation key |
| activation_keys.destroy | [DELETE /katello/api/activation_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/destroy.html)  | Destroy an activation key |
| activation_keys.host_collections_index | [GET /katello/api/activation_keys/:activation_key_id/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/index.html)  | List host collections in an activation key |
| activation_keys.index | [GET /katello/api/activation_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/index.html)  | List activation keys |
| activation_keys.product_content | [GET /katello/api/activation_keys/:id/product_content](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/product_content.html)  | Show content available for an activation key |
| activation_keys.products_index | [GET /katello/api/activation_keys/:activation_key_id/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List of subscription products in an activation key |
| activation_keys.remove_host_collections | [PUT /katello/api/activation_keys/:id/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/remove_host_collections.html)  |  |
| activation_keys.remove_subscriptions | [PUT /katello/api/activation_keys/:id/remove_subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/remove_subscriptions.html)  | Unattach a subscription |
| activation_keys.show | [GET /katello/api/activation_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/show.html)  | Show an activation key |
| activation_keys.subscriptions_create | [POST /katello/api/activation_keys/:activation_key_id/subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/create.html)  | Add a subscription to an activation key |
| activation_keys.subscriptions_index | [GET /katello/api/activation_keys/:activation_key_id/subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/index.html)  | List an activation key's subscriptions |
| activation_keys.update | [PUT /katello/api/activation_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/update.html)  | Update an activation key |
| ansible_collections.compare | [GET /katello/api/ansible_collections/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ansible_collections/compare.html)  | List :resource |
| ansible_collections.index | [GET /katello/api/ansible_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ansible_collections/index.html)  | List ansible_collections |
| ansible_collections.show | [GET /katello/api/ansible_collections/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ansible_collections/show.html)  | Show an ansible collection |
| ansible_inventories.hosts | [POST /api/ansible_inventories/hosts](https://theforeman.org/api/1.16/apidoc/v2/ansible_inventories/hosts.html)  | Show Ansible inventory for hosts |
| ansible_inventories.schedule | [POST /api/ansible_inventories/schedule](https://theforeman.org/api/1.16/apidoc/v2/ansible_inventories/schedule.html)  | Schedule generating of Ansible Inventory report |
| api.home_index | [GET /api](https://theforeman.org/api/1.16/apidoc/v2/home/index.html)  | Show available API links |
| architectures.create | [POST /api/architectures](https://theforeman.org/api/1.16/apidoc/v2/architectures/create.html)  | Create an architecture |
| architectures.destroy | [DELETE /api/architectures/:id](https://theforeman.org/api/1.16/apidoc/v2/architectures/destroy.html)  | Delete an architecture |
| architectures.images_architecture_id_showimages | [GET /api/architectures/:architecture_id/images/:id](https://theforeman.org/api/1.16/apidoc/v2/images/show.html)  | Show an image |
| architectures.images_index | [GET /api/architectures/:architecture_id/images](https://theforeman.org/api/1.16/apidoc/v2/images/index.html)  | List all images for architecture |
| architectures.index | [GET /api/architectures](https://theforeman.org/api/1.16/apidoc/v2/architectures/index.html)  | List all architectures |
| architectures.operatingsystems_index | [GET /api/architectures/:architecture_id/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems for nested architecture |
| architectures.show | [GET /api/architectures/:id](https://theforeman.org/api/1.16/apidoc/v2/architectures/show.html)  | Show an architecture |
| architectures.update | [PUT /api/architectures/:id](https://theforeman.org/api/1.16/apidoc/v2/architectures/update.html)  | Update an architecture |
| audits.index | [GET /api/audits](https://theforeman.org/api/1.16/apidoc/v2/audits/index.html)  | List all audits |
| audits.show | [GET /api/audits/:id](https://theforeman.org/api/1.16/apidoc/v2/audits/show.html)  | Show an audit |
| auth_source_externals.index | [GET /api/auth_source_externals](https://theforeman.org/api/1.16/apidoc/v2/auth_source_externals/index.html)  | List external authentication sources |
| auth_source_externals.show | [GET /api/auth_source_externals/:id](https://theforeman.org/api/1.16/apidoc/v2/auth_source_externals/show.html)  | Show an external authentication source |
| auth_source_externals.update | [PUT /api/auth_source_externals/:id](https://theforeman.org/api/1.16/apidoc/v2/auth_source_externals/update.html)  | Update an external authentication source |
| auth_source_externals.users_index | [GET /api/auth_source_externals/:auth_source_external_id/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users for external authentication source |
| auth_source_internals.index | [GET /api/auth_source_internals](https://theforeman.org/api/1.16/apidoc/v2/auth_source_internals/index.html)  | List internal authentication sources |
| auth_source_internals.show | [GET /api/auth_source_internals/:id](https://theforeman.org/api/1.16/apidoc/v2/auth_source_internals/show.html)  | Show an internal authentication source |
| auth_source_ldaps.create | [POST /api/auth_source_ldaps](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/create.html)  | Create an LDAP authentication source |
| auth_source_ldaps.destroy | [DELETE /api/auth_source_ldaps/:id](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/destroy.html)  | Delete an LDAP authentication source |
| auth_source_ldaps.external_usergroups_auth_source_ldap_id_external_showusergroups | [GET /api/auth_source_ldaps/:auth_source_ldap_id/external_usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/show.html)  | Show an external user group for LDAP authentication source |
| auth_source_ldaps.external_usergroups_index | [GET /api/auth_source_ldaps/:auth_source_ldap_id/external_usergroups](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/index.html)  | List all external user groups for LDAP authentication source |
| auth_source_ldaps.index | [GET /api/auth_source_ldaps](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/index.html)  | List all LDAP authentication sources |
| auth_source_ldaps.show | [GET /api/auth_source_ldaps/:id](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/show.html)  | Show an LDAP authentication source |
| auth_source_ldaps.test | [PUT /api/auth_source_ldaps/:id/test](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/test.html)  | Test LDAP connection |
| auth_source_ldaps.update | [PUT /api/auth_source_ldaps/:id](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/update.html)  | Update an LDAP authentication source |
| auth_source_ldaps.users_index | [GET /api/auth_source_ldaps/:auth_source_ldap_id/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users for LDAP authentication source |
| auth_sources.index | [GET /api/auth_sources](https://theforeman.org/api/1.16/apidoc/v2/auth_sources/index.html)  | List all authentication sources |
| bookmarks.create | [POST /api/bookmarks](https://theforeman.org/api/1.16/apidoc/v2/bookmarks/create.html)  | Create a bookmark |
| bookmarks.destroy | [DELETE /api/bookmarks/:id](https://theforeman.org/api/1.16/apidoc/v2/bookmarks/destroy.html)  | Delete a bookmark |
| bookmarks.index | [GET /api/bookmarks](https://theforeman.org/api/1.16/apidoc/v2/bookmarks/index.html)  | List all bookmarks |
| bookmarks.show | [GET /api/bookmarks/:id](https://theforeman.org/api/1.16/apidoc/v2/bookmarks/show.html)  | Show a bookmark |
| bookmarks.update | [PUT /api/bookmarks/:id](https://theforeman.org/api/1.16/apidoc/v2/bookmarks/update.html)  | Update a bookmark |
| capsules.capsule_content_add_lifecycle_environment | [POST /katello/api/capsules/:id/content/lifecycle_environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/add_lifecycle_environment.html)  | Add lifecycle environments to the smart proxy |
| capsules.capsule_content_apsules | [DELETE /katello/api/capsules/:id/content/lifecycle_environments/:environment_id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/remove_lifecycle_environment.html)  | Remove lifecycle environments from the smart proxy |
| capsules.capsule_content_available_lifecycle_environments | [GET /katello/api/capsules/:id/content/available_lifecycle_environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/available_lifecycle_environments.html)  | List the lifecycle environments not attached to the smart proxy |
| capsules.capsule_content_cancel_sync | [DELETE /katello/api/capsules/:id/content/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/cancel_sync.html)  | Cancel running smart proxy synchronization |
| capsules.capsule_content_lifecycle_environments | [GET /katello/api/capsules/:id/content/lifecycle_environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/lifecycle_environments.html)  | List the lifecycle environments attached to the smart proxy |
| capsules.capsule_content_sync | [POST /katello/api/capsules/:id/content/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/sync.html)  | Synchronize the content to the smart proxy |
| capsules.capsule_content_sync_status | [GET /katello/api/capsules/:id/content/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/sync_status.html)  | Get current smart proxy synchronization status |
| capsules.index | [GET /katello/api/capsules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsules/index.html)  | List all smart proxies that have content |
| capsules.show | [GET /katello/api/capsules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsules/show.html)  | Show the smart proxy details |
| common_parameters.create | [POST /api/common_parameters](https://theforeman.org/api/1.16/apidoc/v2/common_parameters/create.html)  | Create a global parameter |
| common_parameters.destroy | [DELETE /api/common_parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/common_parameters/destroy.html)  | Delete a global parameter |
| common_parameters.index | [GET /api/common_parameters](https://theforeman.org/api/1.16/apidoc/v2/common_parameters/index.html)  | List all global parameters |
| common_parameters.show | [GET /api/common_parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/common_parameters/show.html)  | Show a global parameter |
| common_parameters.update | [PUT /api/common_parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/common_parameters/update.html)  | Update a global parameter |
| compute_attributes.create | [POST /api/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/create.html)  | Create a compute attributes set |
| compute_attributes.index | [GET /api/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/index.html)  | List of compute attributes |
| compute_attributes.show | [GET /api/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/show.html)  | Show a compute attributes set |
| compute_attributes.update | [PUT /api/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/update.html)  | Update a compute attributes set |
| compute_profiles.compute_attributes_compute_profile_id_compute_createresources | [POST /api/compute_profiles/:compute_profile_id/compute_resources/:compute_resource_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/create.html)  | Create a compute attributes set |
| compute_profiles.compute_attributes_compute_profile_id_compute_indexresources | [GET /api/compute_profiles/:compute_profile_id/compute_resources/:compute_resource_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/index.html)  | List of compute attributes for provided compute profile and compute resource |
| compute_profiles.compute_attributes_compute_profile_id_compute_showattributes | [GET /api/compute_profiles/:compute_profile_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/show.html)  | Show a compute attributes set |
| compute_profiles.compute_attributes_compute_profile_id_compute_showresources | [GET /api/compute_profiles/:compute_profile_id/compute_resources/:compute_resource_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/show.html)  | Show a compute attributes set |
| compute_profiles.compute_attributes_compute_profile_id_compute_updateattributes | [PUT /api/compute_profiles/:compute_profile_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/update.html)  | Update a compute attributes set |
| compute_profiles.compute_attributes_compute_profile_id_compute_updateresources | [PUT /api/compute_profiles/:compute_profile_id/compute_resources/:compute_resource_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/update.html)  | Update a compute attributes set |
| compute_profiles.compute_attributes_create | [POST /api/compute_profiles/:compute_profile_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/create.html)  | Create a compute attributes set |
| compute_profiles.compute_attributes_index | [GET /api/compute_profiles/:compute_profile_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/index.html)  | List of compute attributes for compute profile |
| compute_profiles.create | [POST /api/compute_profiles](https://theforeman.org/api/1.16/apidoc/v2/compute_profiles/create.html)  | Create a compute profile |
| compute_profiles.destroy | [DELETE /api/compute_profiles/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_profiles/destroy.html)  | Delete a compute profile |
| compute_profiles.index | [GET /api/compute_profiles](https://theforeman.org/api/1.16/apidoc/v2/compute_profiles/index.html)  | List of compute profiles |
| compute_profiles.show | [GET /api/compute_profiles/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_profiles/show.html)  | Show a compute profile |
| compute_profiles.update | [PUT /api/compute_profiles/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_profiles/update.html)  | Update a compute profile |
| compute_resources.associate | [PUT /api/compute_resources/:id/associate](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/associate.html)  | Associate VMs to Hosts |
| compute_resources.available_clusters | [GET /api/compute_resources/:id/available_clusters](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_clusters.html)  | List available clusters for a compute resource |
| compute_resources.available_flavors | [GET /api/compute_resources/:id/available_flavors](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_flavors.html)  | List available flavors for a compute resource |
| compute_resources.available_folders | [GET /api/compute_resources/:id/available_folders](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_folders.html)  | List available folders for a compute resource |
| compute_resources.available_images | [GET /api/compute_resources/:id/available_images](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_images.html)  | List available images for a compute resource |
| compute_resources.available_networks | [GET /api/compute_resources/:id/available_networks](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_networks.html)  | List available networks for a compute resource |
| compute_resources.available_security_groups | [GET /api/compute_resources/:id/available_security_groups](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_security_groups.html)  | List available security groups for a compute resource |
| compute_resources.available_storage_domains | [GET /api/compute_resources/:id/available_storage_domains](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_storage_domains.html)  | List storage domains for a compute resource |
| compute_resources.available_storage_pods | [GET /api/compute_resources/:id/available_storage_pods](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_storage_pods.html)  | List storage pods for a compute resource |
| compute_resources.available_zones | [GET /api/compute_resources/:id/available_zones](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_zones.html)  | List available zone for a compute resource |
| compute_resources.compute_attributes_compute_resource_id_compute_createprofiles | [POST /api/compute_resources/:compute_resource_id/compute_profiles/:compute_profile_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/create.html)  | Create a compute attributes set |
| compute_resources.compute_attributes_compute_resource_id_compute_indexprofiles | [GET /api/compute_resources/:compute_resource_id/compute_profiles/:compute_profile_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/index.html)  | List of compute attributes for provided compute profile and compute resource |
| compute_resources.compute_attributes_compute_resource_id_compute_showattributes | [GET /api/compute_resources/:compute_resource_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/show.html)  | Show a compute attributes set |
| compute_resources.compute_attributes_compute_resource_id_compute_showprofiles | [GET /api/compute_resources/:compute_resource_id/compute_profiles/:compute_profile_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/show.html)  | Show a compute attributes set |
| compute_resources.compute_attributes_compute_resource_id_compute_updateattributes | [PUT /api/compute_resources/:compute_resource_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/update.html)  | Update a compute attributes set |
| compute_resources.compute_attributes_compute_resource_id_compute_updateprofiles | [PUT /api/compute_resources/:compute_resource_id/compute_profiles/:compute_profile_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/update.html)  | Update a compute attributes set |
| compute_resources.compute_attributes_create | [POST /api/compute_resources/:compute_resource_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/create.html)  | Create a compute attributes set |
| compute_resources.compute_attributes_index | [GET /api/compute_resources/:compute_resource_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/index.html)  | List of compute attributes for compute resource |
| compute_resources.create | [POST /api/compute_resources](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/create.html)  | Create a compute resource |
| compute_resources.destroy | [DELETE /api/compute_resources/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/destroy.html)  | Delete a compute resource |
| compute_resources.id_available_available_networksclusters | [GET /api/compute_resources/:id/available_clusters/:cluster_id/available_networks](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_networks.html)  | List available networks for a compute resource cluster |
| compute_resources.id_available_available_resource_poolsclusters | [GET /api/compute_resources/:id/available_clusters/:cluster_id/available_resource_pools](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_resource_pools.html)  | List resource pools for a compute resource cluster |
| compute_resources.id_available_available_storage_domainsclusters | [GET /api/compute_resources/:id/available_clusters/:cluster_id/available_storage_domains](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_storage_domains.html)  | List storage domains for a compute resource |
| compute_resources.id_available_available_storage_podsclusters | [GET /api/compute_resources/:id/available_clusters/:cluster_id/available_storage_pods](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_storage_pods.html)  | List storage pods for a compute resource |
| compute_resources.id_available_storage_available_storage_domainsdomains | [GET /api/compute_resources/:id/available_storage_domains/:storage_domain](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_storage_domains.html)  | List attributes for a given storage domain |
| compute_resources.id_available_storage_available_storage_podspods | [GET /api/compute_resources/:id/available_storage_pods/:storage_pod](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_storage_pods.html)  | List attributes for a given storage pod |
| compute_resources.id_storage_storage_domaindomains | [GET /api/compute_resources/:id/storage_domains/:storage_domain_id](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/storage_domain.html)  | List attributes for a given storage domain |
| compute_resources.id_storage_storage_podpods | [GET /api/compute_resources/:id/storage_pods/:storage_pod_id](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/storage_pod.html)  | List attributes for a given storage pod |
| compute_resources.images_compute_resource_id_destroyimages | [DELETE /api/compute_resources/:compute_resource_id/images/:id](https://theforeman.org/api/1.16/apidoc/v2/images/destroy.html)  | Delete an image |
| compute_resources.images_compute_resource_id_showimages | [GET /api/compute_resources/:compute_resource_id/images/:id](https://theforeman.org/api/1.16/apidoc/v2/images/show.html)  | Show an image |
| compute_resources.images_compute_resource_id_updateimages | [PUT /api/compute_resources/:compute_resource_id/images/:id](https://theforeman.org/api/1.16/apidoc/v2/images/update.html)  | Update an image |
| compute_resources.images_create | [POST /api/compute_resources/:compute_resource_id/images](https://theforeman.org/api/1.16/apidoc/v2/images/create.html)  | Create an image |
| compute_resources.images_index | [GET /api/compute_resources/:compute_resource_id/images](https://theforeman.org/api/1.16/apidoc/v2/images/index.html)  | List all images for a compute resource |
| compute_resources.index | [GET /api/compute_resources](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/index.html)  | List all compute resources |
| compute_resources.refresh_cache | [PUT /api/compute_resources/:id/refresh_cache](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/refresh_cache.html)  | Refresh Compute Resource Cache |
| compute_resources.show | [GET /api/compute_resources/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/show.html)  | Show a compute resource |
| compute_resources.update | [PUT /api/compute_resources/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/update.html)  | Update a compute resource |
| config_groups.create | [POST /api/config_groups](https://theforeman.org/api/1.16/apidoc/v2/config_groups/create.html)  | Create a config group |
| config_groups.destroy | [DELETE /api/config_groups/:id](https://theforeman.org/api/1.16/apidoc/v2/config_groups/destroy.html)  | Delete a config group |
| config_groups.index | [GET /api/config_groups](https://theforeman.org/api/1.16/apidoc/v2/config_groups/index.html)  | List of config groups |
| config_groups.show | [GET /api/config_groups/:id](https://theforeman.org/api/1.16/apidoc/v2/config_groups/show.html)  | Show a config group |
| config_groups.update | [PUT /api/config_groups/:id](https://theforeman.org/api/1.16/apidoc/v2/config_groups/update.html)  | Update a config group |
| config_reports.create | [POST /api/config_reports](https://theforeman.org/api/1.16/apidoc/v2/config_reports/create.html)  | Create a report |
| config_reports.destroy | [DELETE /api/config_reports/:id](https://theforeman.org/api/1.16/apidoc/v2/config_reports/destroy.html)  | Delete a report |
| config_reports.index | [GET /api/config_reports](https://theforeman.org/api/1.16/apidoc/v2/config_reports/index.html)  | List all reports |
| config_reports.show | [GET /api/config_reports/:id](https://theforeman.org/api/1.16/apidoc/v2/config_reports/show.html)  | Show a report |
| config_templates.build_pxe_default | [POST /api/config_templates/build_pxe_default](https://theforeman.org/api/1.16/apidoc/v2/config_templates/build_pxe_default.html)  | Update the default PXE menu on all configured TFTP servers |
| config_templates.clone | [POST /api/config_templates/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/config_templates/clone.html)  | Clone a provision template |
| config_templates.create | [POST /api/config_templates](https://theforeman.org/api/1.16/apidoc/v2/config_templates/create.html)  | Create a provisioning template |
| config_templates.destroy | [DELETE /api/config_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/config_templates/destroy.html)  | Delete a provisioning template |
| config_templates.index | [GET /api/config_templates](https://theforeman.org/api/1.16/apidoc/v2/config_templates/index.html)  | List provisioning templates |
| config_templates.operatingsystems_index | [GET /api/config_templates/:config_template_id/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems for nested provisioning template |
| config_templates.os_default_templates_index | [GET /api/config_templates/:config_template_id/os_default_templates](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/index.html)  | List operating systems where this template is set as a default |
| config_templates.revision | [GET /api/config_templates/revision](https://theforeman.org/api/1.16/apidoc/v2/config_templates/revision.html)  |  |
| config_templates.show | [GET /api/config_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/config_templates/show.html)  | Show provisioning template details |
| config_templates.template_combinations_config_template_id_template_showcombinations | [GET /api/config_templates/:config_template_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/show.html)  | Show template combination |
| config_templates.template_combinations_config_template_id_template_updatecombinations | [PUT /api/config_templates/:config_template_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/update.html)  | Update template combination |
| config_templates.template_combinations_create | [POST /api/config_templates/:config_template_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/create.html)  | Add a template combination |
| config_templates.template_combinations_index | [GET /api/config_templates/:config_template_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/index.html)  | List template combination |
| config_templates.update | [PUT /api/config_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/config_templates/update.html)  | Update a provisioning template |
| content_credentials.content | [GET /katello/api/content_credentials/:id/content](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_credentials/content.html)  | Return the content of a content credential, used directly by yum |
| content_credentials.create | [POST /katello/api/content_credentials](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_credentials/create.html)  | Create a content credential |
| content_credentials.destroy | [DELETE /katello/api/content_credentials/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_credentials/destroy.html)  | Destroy a content credential |
| content_credentials.index | [GET /katello/api/content_credentials](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_credentials/index.html)  | List content credentials |
| content_credentials.set_content | [POST /katello/api/content_credentials/:id/content](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_credentials/set_content.html)  | Upload content credential contents |
| content_credentials.show | [GET /katello/api/content_credentials/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_credentials/show.html)  | Show a content credential |
| content_credentials.update | [PUT /katello/api/content_credentials/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_credentials/update.html)  | Update a content credential |
| content_view_filters.ansible_collections_index | [GET /katello/api/content_view_filters/:content_view_filter_id/ansible_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ansible_collections/index.html)  | List ansible_collections |
| content_view_filters.content_view_filter_rules_create | [POST /katello/api/content_view_filters/:content_view_filter_id/rules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filter_rules/create.html)  | Create a filter rule. The parameters included should be based upon the filter type. |
| content_view_filters.content_view_filter_rules_index | [GET /katello/api/content_view_filters/:content_view_filter_id/rules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filter_rules/index.html)  | List filter rules |
| content_view_filters.content_view_filter_rules_ontent_view_destroyfilters | [DELETE /katello/api/content_view_filters/:content_view_filter_id/rules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filter_rules/destroy.html)  | Delete a filter rule |
| content_view_filters.content_view_filter_rules_ontent_view_showfilters | [GET /katello/api/content_view_filters/:content_view_filter_id/rules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filter_rules/show.html)  | Show filter rule info |
| content_view_filters.content_view_filter_rules_ontent_view_updatefilters | [PUT /katello/api/content_view_filters/:content_view_filter_id/rules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filter_rules/update.html)  | Update a filter rule. The parameters included should be based upon the filter type. |
| content_view_filters.create | [post /katello/api/content_view_filters](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/create.html)  | create a filter for a content view |
| content_view_filters.debs_index | [GET /katello/api/content_view_filters/:content_view_filter_id/debs](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/debs/index.html)  | List deb packages |
| content_view_filters.destroy | [delete /katello/api/content_view_filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/destroy.html)  | delete a filter |
| content_view_filters.docker_manifest_lists_index | [GET /katello/api/content_view_filters/:content_view_filter_id/docker_manifest_lists](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifest_lists/index.html)  | List docker_manifest_lists |
| content_view_filters.docker_manifests_index | [GET /katello/api/content_view_filters/:content_view_filter_id/docker_manifests](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/index.html)  | List docker_manifests |
| content_view_filters.docker_tags_index | [GET /katello/api/content_view_filters/:content_view_filter_id/docker_tags](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/index.html)  | List docker_tags |
| content_view_filters.file_units_index | [GET /katello/api/content_view_filters/:content_view_filter_id/files](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/file_units/index.html)  | List files |
| content_view_filters.index | [get /katello/api/content_view_filters](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/index.html)  | list filters |
| content_view_filters.module_streams_index | [GET /katello/api/content_view_filters/:content_view_filter_id/module_streams](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/module_streams/index.html)  | List module_streams |
| content_view_filters.ostree_branches_index | [GET /katello/api/content_view_filters/:content_view_filter_id/ostree_branches](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/index.html)  | List ostree_branches |
| content_view_filters.package_groups_index | [GET /katello/api/content_view_filters/:content_view_filter_id/package_groups](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/index.html)  | List package_groups |
| content_view_filters.packages_ontent_view_indexfilters | [GET /katello/api/content_view_filters/:content_view_filter_id/:resource_id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/index.html)  | List :resource_id |
| content_view_filters.puppet_modules_index | [GET /katello/api/content_view_filters/:content_view_filter_id/puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/index.html)  | List puppet_modules |
| content_view_filters.show | [get /katello/api/content_view_filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/show.html)  | show filter info |
| content_view_filters.update | [put /katello/api/content_view_filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/update.html)  | update a filter |
| content_view_versions.destroy | [DELETE /katello/api/content_view_versions/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/destroy.html)  | Remove content view version |
| content_view_versions.errata_available_errata | [GET /katello/api/content_view_versions/:id/available_errata](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/errata/available_errata.html)  | Return errata that can be added to the Content View Version via an Incremental Update |
| content_view_versions.export | [POST /katello/api/content_view_versions/:id/export](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/export.html)  | Export a content view version |
| content_view_versions.incremental_update | [POST /katello/api/content_view_versions/incremental_update](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/incremental_update.html)  | Perform an Incremental Update on one or more Content View Versions |
| content_view_versions.index | [GET /katello/api/content_view_versions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/index.html)  | List content view versions |
| content_view_versions.promote | [POST /katello/api/content_view_versions/:id/promote](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/promote.html)  | Promote a content view version |
| content_view_versions.republish_repositories | [PUT /katello/api/content_view_versions/:id/republish_repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/republish_repositories.html)  | Forces a republish of the version's repositories' metadata |
| content_view_versions.show | [GET /katello/api/content_view_versions/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/show.html)  | Show content view version |
| content_view_versions.update | [PUT /katello/api/content_view_versions/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/update.html)  | Update a content view version |
| content_views.ansible_collections_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/ansible_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ansible_collections/index.html)  | List ansible_collections |
| content_views.available_puppet_module_names | [GET /katello/api/content_views/:id/available_puppet_module_names](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/available_puppet_module_names.html)  | Get puppet modules names that are available to be added to the content view |
| content_views.available_puppet_modules | [GET /katello/api/content_views/:id/available_puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/available_puppet_modules.html)  | Get puppet modules that are available to be added to the content view |
| content_views.content_view_components_add_components | [PUT /katello/api/content_views/:composite_content_view_id/content_view_components/add](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_components/add_components.html)  | Add components to the content view |
| content_views.content_view_components_index | [GET /katello/api/content_views/:composite_content_view_id/content_view_components](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_components/index.html)  | List components attached to this content view |
| content_views.content_view_components_ontent_showviews | [GET /katello/api/content_views/:composite_content_view_id/content_view_components/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_components/show.html)  | Show a content view component |
| content_views.content_view_components_ontent_updateviews | [PUT /katello/api/content_views/:composite_content_view_id/content_view_components/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_components/update.html)  | Update a component associated with the content view |
| content_views.content_view_components_remove_components | [PUT /katello/api/content_views/:composite_content_view_id/content_view_components/remove](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_components/remove_components.html)  | Remove components from the content view |
| content_views.content_view_filters_create | [post /katello/api/content_views/:content_view_id/filters](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/create.html)  | create a filter for a content view |
| content_views.content_view_filters_index | [get /katello/api/content_views/:content_view_id/filters](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/index.html)  | list filters |
| content_views.content_view_filters_ontent_destroyviews | [delete /katello/api/content_views/:content_view_id/filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/destroy.html)  | delete a filter |
| content_views.content_view_filters_ontent_showviews | [get /katello/api/content_views/:content_view_id/filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/show.html)  | show filter info |
| content_views.content_view_filters_ontent_updateviews | [put /katello/api/content_views/:content_view_id/filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/update.html)  | update a filter |
| content_views.content_view_histories_index | [GET /katello/api/content_views/:id/history](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_histories/index.html)  | Show a content view's history |
| content_views.content_view_puppet_modules_create | [POST /katello/api/content_views/:content_view_id/content_view_puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_puppet_modules/create.html)  | Add a puppet module to the content view |
| content_views.content_view_puppet_modules_index | [GET /katello/api/content_views/:content_view_id/content_view_puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_puppet_modules/index.html)  | List content view puppet modules |
| content_views.content_view_puppet_modules_ontent_destroyviews | [DELETE /katello/api/content_views/:content_view_id/content_view_puppet_modules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_puppet_modules/destroy.html)  | Remove a puppet module from the content view |
| content_views.content_view_puppet_modules_ontent_showviews | [GET /katello/api/content_views/:content_view_id/content_view_puppet_modules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_puppet_modules/show.html)  | Show a content view puppet module |
| content_views.content_view_puppet_modules_ontent_updateviews | [PUT /katello/api/content_views/:content_view_id/content_view_puppet_modules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_puppet_modules/update.html)  | Update a puppet module associated with the content view |
| content_views.content_view_versions_index | [GET /katello/api/content_views/:content_view_id/content_view_versions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/index.html)  | List content view versions |
| content_views.copy | [POST /katello/api/content_views/:id/copy](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/copy.html)  | Make copy of a content view |
| content_views.create | [POST /katello/api/content_views](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/create.html)  | Create a content view |
| content_views.debs_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/debs](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/debs/index.html)  | List deb packages |
| content_views.destroy | [DELETE /katello/api/content_views/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/destroy.html)  | Delete a content view |
| content_views.docker_manifest_lists_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/docker_manifest_lists](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifest_lists/index.html)  | List docker_manifest_lists |
| content_views.docker_manifests_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/docker_manifests](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/index.html)  | List docker_manifests |
| content_views.docker_tags_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/docker_tags](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/index.html)  | List docker_tags |
| content_views.file_units_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/files](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/file_units/index.html)  | List files |
| content_views.index | [GET /katello/api/content_views](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/index.html)  | List content views |
| content_views.module_streams_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/module_streams](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/module_streams/index.html)  | List module_streams |
| content_views.ontent_remove_from_environmentviews | [DELETE /katello/api/content_views/:id/environments/:environment_id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/remove_from_environment.html)  | Remove a content view from an environment |
| content_views.ostree_branches_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/ostree_branches](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/index.html)  | List ostree_branches |
| content_views.package_groups_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/package_groups](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/index.html)  | List package_groups |
| content_views.packages_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/:resource_id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/index.html)  | List :resource_id |
| content_views.publish | [POST /katello/api/content_views/:id/publish](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/publish.html)  | Publish a content view |
| content_views.puppet_modules_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/index.html)  | List puppet_modules |
| content_views.remove | [PUT /katello/api/content_views/:id/remove](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/remove.html)  | Remove versions and/or environments from a content view and reassign systems and keys |
| content_views.repositories_index | [GET /katello/api/content_views/:id/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/index.html)  | List of repositories for a content view |
| content_views.show | [GET /katello/api/content_views/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/show.html)  | Show a content view |
| content_views.update | [PUT /katello/api/content_views/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/update.html)  | Update a content view |
| current_user.users_show_current | [GET /api/current_user](https://theforeman.org/api/1.16/apidoc/v2/users/show_current.html)  | Show the currently logged-in user |
| dashboard.index | [GET /api/dashboard](https://theforeman.org/api/1.16/apidoc/v2/dashboard/index.html)  | Get dashboard details |
| debs.compare | [GET /katello/api/debs/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/debs/compare.html)  | List deb packages |
| debs.index | [GET /katello/api/debs](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/debs/index.html)  | List deb packages |
| debs.show | [GET /katello/api/debs/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/debs/show.html)  | Show a deb package |
| discovered_hosts.auto_provision | [POST /api/v2/discovered_hosts/:id/auto_provision](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/auto_provision.html)  | Execute rules against a discovered host |
| discovered_hosts.auto_provision_all | [POST /api/v2/discovered_hosts/auto_provision_all](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/auto_provision_all.html)  | Execute rules against all currently discovered hosts |
| discovered_hosts.create | [POST /api/v2/discovered_hosts](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/create.html)  | Create a discovered host for testing (use /facts to create new hosts) |
| discovered_hosts.destroy | [DELETE /api/v2/discovered_hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/destroy.html)  | Delete a discovered host |
| discovered_hosts.facts | [POST /api/v2/discovered_hosts/facts](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/facts.html)  | Upload facts for a host, creating the host if required |
| discovered_hosts.index | [GET /api/v2/discovered_hosts](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/index.html)  | List all discovered hosts |
| discovered_hosts.reboot | [PUT /api/v2/discovered_hosts/:id/reboot](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/reboot.html)  | Rebooting a discovered host |
| discovered_hosts.reboot_all | [PUT /api/v2/discovered_hosts/reboot_all](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/reboot_all.html)  | Rebooting all discovered hosts |
| discovered_hosts.refresh_facts | [PUT /api/v2/discovered_hosts/:id/refresh_facts](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/refresh_facts.html)  | Refreshing the facts of a discovered host |
| discovered_hosts.show | [GET /api/v2/discovered_hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/show.html)  | Show a discovered host |
| discovered_hosts.update | [PUT /api/v2/discovered_hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/update.html)  | Provision a discovered host |
| discovery_rules.create | [POST /api/v2/discovery_rules](https://theforeman.org/api/1.16/apidoc/v2/discovery_rules/create.html)  | Create a discovery rule |
| discovery_rules.destroy | [DELETE /api/v2/discovery_rules/:id](https://theforeman.org/api/1.16/apidoc/v2/discovery_rules/destroy.html)  | Delete a rule |
| discovery_rules.index | [GET /api/v2/discovery_rules](https://theforeman.org/api/1.16/apidoc/v2/discovery_rules/index.html)  | List all discovery rules |
| discovery_rules.show | [GET /api/v2/discovery_rules/:id](https://theforeman.org/api/1.16/apidoc/v2/discovery_rules/show.html)  | Show a discovery rule |
| discovery_rules.update | [PUT /api/v2/discovery_rules/:id](https://theforeman.org/api/1.16/apidoc/v2/discovery_rules/update.html)  | Update a rule |
| docker_manifest_lists.compare | [GET /katello/api/docker_manifest_lists/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifest_lists/compare.html)  | List docker_manifest_lists |
| docker_manifest_lists.index | [GET /katello/api/docker_manifest_lists](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifest_lists/index.html)  | List docker_manifest_lists |
| docker_manifest_lists.show | [GET /katello/api/docker_manifest_lists/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifest_lists/show.html)  | Show a docker manifest list |
| docker_manifests.compare | [GET /katello/api/docker_manifests/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/compare.html)  | List docker_manifests |
| docker_manifests.index | [GET /katello/api/docker_manifests](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/index.html)  | List docker_manifests |
| docker_manifests.show | [GET /katello/api/docker_manifests/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/show.html)  | Show a docker manifest |
| docker_tags.compare | [GET /katello/api/docker_tags/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/compare.html)  | List docker_tags |
| docker_tags.index | [GET /katello/api/docker_tags](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/index.html)  | List docker_tags |
| docker_tags.show | [GET /katello/api/docker_tags/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/show.html)  | Show a docker tag |
| domains.create | [POST /api/domains](https://theforeman.org/api/1.16/apidoc/v2/domains/create.html)  | Create a domain |
| domains.destroy | [DELETE /api/domains/:id](https://theforeman.org/api/1.16/apidoc/v2/domains/destroy.html)  | Delete a domain |
| domains.index | [GET /api/domains](https://theforeman.org/api/1.16/apidoc/v2/domains/index.html)  | List of domains |
| domains.interfaces_index | [GET /api/domains/:domain_id/interfaces](https://theforeman.org/api/1.16/apidoc/v2/interfaces/index.html)  | List all interfaces for domain |
| domains.parameters_create | [POST /api/domains/:domain_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for a domain |
| domains.parameters_domain_id_destroyparameters | [DELETE /api/domains/:domain_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for a domain |
| domains.parameters_domain_id_showparameters | [GET /api/domains/:domain_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for a domain |
| domains.parameters_domain_id_updateparameters | [PUT /api/domains/:domain_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for a domain |
| domains.parameters_index | [GET /api/domains/:domain_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for a domain |
| domains.parameters_reset | [DELETE /api/domains/:domain_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameters for a domain |
| domains.show | [GET /api/domains/:id](https://theforeman.org/api/1.16/apidoc/v2/domains/show.html)  | Show a domain |
| domains.subnets_index | [GET /api/domains/:domain_id/subnets](https://theforeman.org/api/1.16/apidoc/v2/subnets/index.html)  | List of subnets for a domain |
| domains.update | [PUT /api/domains/:id](https://theforeman.org/api/1.16/apidoc/v2/domains/update.html)  | Update a domain |
| environments.activation_keys_index | [GET /katello/api/environments/:environment_id/activation_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/index.html)  |  |
| environments.create | [POST /api/environments](https://theforeman.org/api/1.16/apidoc/v2/environments/create.html)  | Create an environment |
| environments.destroy | [DELETE /api/environments/:id](https://theforeman.org/api/1.16/apidoc/v2/environments/destroy.html)  | Delete an environment |
| environments.environment_id_smart_import_puppetclassesproxies | [POST /api/environments/:environment_id/smart_proxies/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/environments/import_puppetclasses.html)  | Import puppet classes from puppet proxy for an environment |
| environments.hosts_index | [GET /api/environments/:environment_id/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/index.html)  | List hosts per environment |
| environments.index | [GET /api/environments](https://theforeman.org/api/1.16/apidoc/v2/environments/index.html)  | List all environments |
| environments.lifecycle_environments_create | [POST /katello/api/environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/create.html)  | Create an environment |
| environments.lifecycle_environments_destroy | [DELETE /katello/api/environments/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/destroy.html)  | Destroy an environment |
| environments.lifecycle_environments_index | [GET /katello/api/environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/index.html)  | List environments in an organization |
| environments.lifecycle_environments_show | [GET /katello/api/environments/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/show.html)  | Show an environment |
| environments.lifecycle_environments_update | [PUT /katello/api/environments/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/update.html)  | Update an environment |
| environments.puppetclasses_environment_id_showpuppetclasses | [GET /api/environments/:environment_id/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/show.html)  | Show a Puppet class for an environment |
| environments.puppetclasses_index | [GET /api/environments/:environment_id/puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/index.html)  | List all Puppet classes for an environment |
| environments.repositories_nvironments | [GET /katello/api/environments/:environment_id/products/:product_id/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/index.html)  | List of repositories belonging to a product in an environment |
| environments.show | [GET /api/environments/:id](https://theforeman.org/api/1.16/apidoc/v2/environments/show.html)  | Show an environment |
| environments.smart_class_parameters_environment_id_indexpuppetclasses | [GET /api/environments/:environment_id/puppetclasses/:puppetclass_id/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List of smart class parameters for a specific environment/Puppet class combination |
| environments.smart_class_parameters_index | [GET /api/environments/:environment_id/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List of smart class parameters for a specific environment |
| environments.smart_proxies_environment_id_smart_import_puppetclassesproxies | [POST /api/environments/:environment_id/smart_proxies/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/import_puppetclasses.html)  | Import puppet classes from puppet proxy for an environment |
| environments.template_combinations_create | [POST /api/environments/:environment_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/create.html)  | Add a template combination |
| environments.template_combinations_environment_id_template_showcombinations | [GET /api/environments/:environment_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/show.html)  | Show template combination |
| environments.template_combinations_environment_id_template_updatecombinations | [PUT /api/environments/:environment_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/update.html)  | Update template combination |
| environments.template_combinations_index | [GET /api/environments/:environment_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/index.html)  | List template combination |
| environments.update | [PUT /api/environments/:id](https://theforeman.org/api/1.16/apidoc/v2/environments/update.html)  | Update an environment |
| errata.compare | [GET /katello/api/errata/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/errata/compare.html)  | List errata |
| errata.index | [GET /katello/api/errata](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/errata/index.html)  | List errata |
| errata.show | [GET /katello/api/errata/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/errata/show.html)  | Show an erratum |
| fact_values.index | [GET /api/fact_values](https://theforeman.org/api/1.16/apidoc/v2/fact_values/index.html)  | List all fact values |
| files.file_units_compare | [GET /katello/api/files/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/file_units/compare.html)  | List :resource |
| files.file_units_index | [GET /katello/api/files](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/file_units/index.html)  | List files |
| files.file_units_show | [GET /katello/api/files/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/file_units/show.html)  | Show a file |
| filters.create | [POST /api/filters](https://theforeman.org/api/1.16/apidoc/v2/filters/create.html)  | Create a filter |
| filters.destroy | [DELETE /api/filters/:id](https://theforeman.org/api/1.16/apidoc/v2/filters/destroy.html)  | Delete a filter |
| filters.index | [GET /api/filters](https://theforeman.org/api/1.16/apidoc/v2/filters/index.html)  | List all filters |
| filters.show | [GET /api/filters/:id](https://theforeman.org/api/1.16/apidoc/v2/filters/show.html)  | Show a filter |
| filters.update | [PUT /api/filters/:id](https://theforeman.org/api/1.16/apidoc/v2/filters/update.html)  | Update a filter |
| gpg_keys.content | [GET /katello/api/gpg_keys/:id/content](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/content.html)  | Return the content of a gpg key, used directly by yum |
| gpg_keys.create | [POST /katello/api/gpg_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/create.html)  | Create a gpg key |
| gpg_keys.destroy | [DELETE /katello/api/gpg_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/destroy.html)  | Destroy a gpg key |
| gpg_keys.index | [GET /katello/api/gpg_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/index.html)  | List gpg keys |
| gpg_keys.set_content | [POST /katello/api/gpg_keys/:id/content](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/set_content.html)  | Upload gpg key contents |
| gpg_keys.show | [GET /katello/api/gpg_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/show.html)  | Show a gpg key |
| gpg_keys.update | [PUT /katello/api/gpg_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/update.html)  | Update a repository |
| host_collections.add_hosts | [PUT /katello/api/host_collections/:id/add_hosts](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/add_hosts.html)  | Add host to the host collection |
| host_collections.copy | [POST /katello/api/host_collections/:id/copy](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/copy.html)  | Make copy of a host collection |
| host_collections.create | [POST /katello/api/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/create.html)  | Create a host collection |
| host_collections.destroy | [DELETE /katello/api/host_collections/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/destroy.html)  | Destroy a host collection |
| host_collections.index | [GET /katello/api/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/index.html)  | List host collections |
| host_collections.remove_hosts | [PUT /katello/api/host_collections/:id/remove_hosts](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/remove_hosts.html)  | Remove hosts from the host collection |
| host_collections.show | [GET /katello/api/host_collections/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/show.html)  | Show a host collection |
| host_collections.update | [PUT /katello/api/host_collections/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/update.html)  | Update a host collection |
| hostgroups.ansible_roles | [GET /api/hostgroups/:id/ansible_roles](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/ansible_roles.html)  | List all Ansible roles for a hostgroup |
| hostgroups.assign_ansible_roles | [POST /api/hostgroups/:id/assign_ansible_roles](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/assign_ansible_roles.html)  | Assigns Ansible roles to a hostgroup |
| hostgroups.clone | [POST /api/hostgroups/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/clone.html)  | Clone a host group |
| hostgroups.create | [POST /api/hostgroups](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/create.html)  | Create a host group |
| hostgroups.destroy | [DELETE /api/hostgroups/:id](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/destroy.html)  | Delete a host group |
| hostgroups.hostgroup_classes_create | [POST /api/hostgroups/:hostgroup_id/puppetclass_ids](https://theforeman.org/api/1.16/apidoc/v2/hostgroup_classes/create.html)  | Add a Puppet class to host group |
| hostgroups.hostgroup_classes_hostgroup_id_puppetclass_destroyids | [DELETE /api/hostgroups/:hostgroup_id/puppetclass_ids/:id](https://theforeman.org/api/1.16/apidoc/v2/hostgroup_classes/destroy.html)  | Remove a Puppet class from host group |
| hostgroups.hostgroup_classes_index | [GET /api/hostgroups/:hostgroup_id/puppetclass_ids](https://theforeman.org/api/1.16/apidoc/v2/hostgroup_classes/index.html)  | List all Puppet class IDs for host group |
| hostgroups.hosts_index | [GET /api/hostgroups/:hostgroup_id/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/index.html)  | List all hosts for a host group |
| hostgroups.index | [GET /api/hostgroups](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/index.html)  | List all host groups |
| hostgroups.multiple_play_roles | [POST /api/hostgroups/multiple_play_roles](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/multiple_play_roles.html)  | Runs all Ansible roles on hostgroups |
| hostgroups.parameters_create | [POST /api/hostgroups/:hostgroup_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for a host group |
| hostgroups.parameters_hostgroup_id_destroyparameters | [DELETE /api/hostgroups/:hostgroup_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for a host group |
| hostgroups.parameters_hostgroup_id_showparameters | [GET /api/hostgroups/:hostgroup_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for a host group |
| hostgroups.parameters_hostgroup_id_updateparameters | [PUT /api/hostgroups/:hostgroup_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for a host group |
| hostgroups.parameters_index | [GET /api/hostgroups/:hostgroup_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for a host group |
| hostgroups.parameters_reset | [DELETE /api/hostgroups/:hostgroup_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameters for a host group |
| hostgroups.play_roles | [POST /api/hostgroups/:id/play_roles](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/play_roles.html)  | Runs all Ansible roles on a hostgroup |
| hostgroups.puppetclasses_hostgroup_id_showpuppetclasses | [GET /api/hostgroups/:hostgroup_id/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/show.html)  | Show a Puppet class for a host group |
| hostgroups.puppetclasses_index | [GET /api/hostgroups/:hostgroup_id/puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/index.html)  | List all Puppet classes for a host group |
| hostgroups.rebuild_config | [PUT /api/hostgroups/:id/rebuild_config](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/rebuild_config.html)  | Rebuild orchestration config |
| hostgroups.show | [GET /api/hostgroups/:id](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/show.html)  | Show a host group |
| hostgroups.smart_class_parameters_index | [GET /api/hostgroups/:hostgroup_id/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List of smart class parameters for a specific host group |
| hostgroups.smart_variables_index | [GET /api/hostgroups/:hostgroup_id/smart_variables](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/index.html)  | List of smart variables for a specific host group |
| hostgroups.template_combinations_create | [POST /api/hostgroups/:hostgroup_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/create.html)  | Add a template combination |
| hostgroups.template_combinations_hostgroup_id_template_showcombinations | [GET /api/hostgroups/:hostgroup_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/show.html)  | Show template combination |
| hostgroups.template_combinations_hostgroup_id_template_updatecombinations | [PUT /api/hostgroups/:hostgroup_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/update.html)  | Update template combination |
| hostgroups.template_combinations_index | [GET /api/hostgroups/:hostgroup_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/index.html)  | List template combination |
| hostgroups.update | [PUT /api/hostgroups/:id](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/update.html)  | Update a host group |
| hosts.ansible_roles | [GET /api/hosts/:id/ansible_roles](https://theforeman.org/api/1.16/apidoc/v2/hosts/ansible_roles.html)  | List all Ansible roles for a host |
| hosts.assign_ansible_roles | [POST /api/hosts/:id/assign_ansible_roles](https://theforeman.org/api/1.16/apidoc/v2/hosts/assign_ansible_roles.html)  | Assigns Ansible roles to a host |
| hosts.audits_index | [GET /api/hosts/:host_id/audits](https://theforeman.org/api/1.16/apidoc/v2/audits/index.html)  | List all audits for a given host |
| hosts.boot | [PUT /api/hosts/:id/boot](https://theforeman.org/api/1.16/apidoc/v2/hosts/boot.html)  | Boot host from specified device |
| hosts.config_reports_last | [GET /api/hosts/:host_id/config_reports/last](https://theforeman.org/api/1.16/apidoc/v2/config_reports/last.html)  | Show the last report for a host |
| hosts.create | [POST /api/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/create.html)  | Create a host |
| hosts.destroy | [DELETE /api/hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/hosts/destroy.html)  | Delete a host |
| hosts.disassociate | [PUT /api/hosts/:id/disassociate](https://theforeman.org/api/1.16/apidoc/v2/hosts/disassociate.html)  | Disassociate the host from a VM |
| hosts.enc | [GET /api/hosts/:id/enc](https://theforeman.org/api/1.16/apidoc/v2/hosts/enc.html)  | Get ENC values of host |
| hosts.fact_values_index | [GET /api/hosts/:host_id/facts](https://theforeman.org/api/1.16/apidoc/v2/fact_values/index.html)  | List all fact values of a given host |
| hosts.facts | [POST /api/hosts/facts](https://theforeman.org/api/1.16/apidoc/v2/hosts/facts.html)  | Upload facts for a host, creating the host if required |
| hosts.host_classes_create | [POST /api/hosts/:host_id/puppetclass_ids](https://theforeman.org/api/1.16/apidoc/v2/host_classes/create.html)  | Add a Puppet class to host |
| hosts.host_classes_host_id_puppetclass_destroyids | [DELETE /api/hosts/:host_id/puppetclass_ids/:id](https://theforeman.org/api/1.16/apidoc/v2/host_classes/destroy.html)  | Remove a Puppet class from host |
| hosts.host_classes_index | [GET /api/hosts/:host_id/puppetclass_ids](https://theforeman.org/api/1.16/apidoc/v2/host_classes/index.html)  | List all Puppet class IDs for host |
| hosts.host_collections | [PUT /api/hosts/:host_id/host_collections](https://theforeman.org/api/1.16/apidoc/v2/hosts/host_collections.html)  | Alter a hosts host collections |
| hosts.host_debs_index | [GET /api/hosts/:host_id/debs](https://theforeman.org/api/1.16/apidoc/v2/host_debs/index.html)  | List deb packages installed on the host |
| hosts.host_errata_applicability | [PUT /api/hosts/:host_id/errata/applicability](https://theforeman.org/api/1.16/apidoc/v2/host_errata/applicability.html)  | Force regenerate applicability. |
| hosts.host_errata_apply | [PUT /api/hosts/:host_id/errata/apply](https://theforeman.org/api/1.16/apidoc/v2/host_errata/apply.html)  | Schedule errata for installation |
| hosts.host_errata_host_id_showerrata | [GET /api/hosts/:host_id/errata/:id](https://theforeman.org/api/1.16/apidoc/v2/host_errata/show.html)  | Retrieve a single errata for a host |
| hosts.host_errata_index | [GET /api/hosts/:host_id/errata](https://theforeman.org/api/1.16/apidoc/v2/host_errata/index.html)  | List errata available for the content host |
| hosts.host_module_streams_index | [GET /api/hosts/:host_id/module_streams](https://theforeman.org/api/1.16/apidoc/v2/host_module_streams/index.html)  | List module streams available to the host |
| hosts.host_packages_index | [GET /api/hosts/:host_id/packages](https://theforeman.org/api/1.16/apidoc/v2/host_packages/index.html)  | List packages installed on the host |
| hosts.host_packages_install | [PUT /api/hosts/:host_id/packages/install](https://theforeman.org/api/1.16/apidoc/v2/host_packages/install.html)  | Install packages remotely |
| hosts.host_packages_remove | [PUT /api/hosts/:host_id/packages/remove](https://theforeman.org/api/1.16/apidoc/v2/host_packages/remove.html)  | Uninstall packages remotely |
| hosts.host_packages_upgrade | [PUT /api/hosts/:host_id/packages/upgrade](https://theforeman.org/api/1.16/apidoc/v2/host_packages/upgrade.html)  | Update packages remotely |
| hosts.host_packages_upgrade_all | [PUT /api/hosts/:host_id/packages/upgrade_all](https://theforeman.org/api/1.16/apidoc/v2/host_packages/upgrade_all.html)  | Update packages remotely |
| hosts.host_subscriptions_add_subscriptions | [PUT /api/hosts/:host_id/subscriptions/add_subscriptions](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/add_subscriptions.html)  | Add a subscription to a host |
| hosts.host_subscriptions_auto_attach | [PUT /api/hosts/:host_id/subscriptions/auto_attach](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/auto_attach.html)  | Trigger an auto-attach of subscriptions |
| hosts.host_subscriptions_available_release_versions | [GET /api/hosts/:host_id/subscriptions/available_release_versions](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/available_release_versions.html)  | Show releases available for the content host |
| hosts.host_subscriptions_content_override | [PUT /api/hosts/:host_id/subscriptions/content_override](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/content_override.html)  | Set content overrides for the host |
| hosts.host_subscriptions_create | [POST /api/hosts/subscriptions](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/create.html)  | Register a host with subscription and information |
| hosts.host_subscriptions_destroy | [DELETE /api/hosts/:host_id/subscriptions](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/destroy.html)  | Unregister the host as a subscription consumer |
| hosts.host_subscriptions_events | [GET /api/hosts/:host_id/subscriptions/events](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/events.html)  | List subscription events for the host |
| hosts.host_subscriptions_index | [GET /api/hosts/:host_id/subscriptions](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/index.html)  | List a host's subscriptions |
| hosts.host_subscriptions_product_content | [GET /api/hosts/:host_id/subscriptions/product_content](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/product_content.html)  | Get content and overrides for the host |
| hosts.host_subscriptions_remove_subscriptions | [PUT /api/hosts/:host_id/subscriptions/remove_subscriptions](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/remove_subscriptions.html)  |  |
| hosts.host_tracer_index | [GET /api/hosts/:host_id/traces](https://theforeman.org/api/1.16/apidoc/v2/host_tracer/index.html)  | List services that need restarting on the host |
| hosts.hosts_bulk_actions_add_subscriptions | [PUT /api/hosts/bulk/add_subscriptions](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/add_subscriptions.html)  | Add subscriptions to one or more hosts |
| hosts.hosts_bulk_actions_applicable_errata | [POST /api/hosts/bulk/applicable_errata](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/applicable_errata.html)  | Fetch applicable errata for a host. |
| hosts.hosts_bulk_actions_auto_attach | [PUT /api/hosts/bulk/auto_attach](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/auto_attach.html)  | Trigger an auto-attach of subscriptions on one or more hosts |
| hosts.hosts_bulk_actions_available_incremental_updates | [POST /api/hosts/bulk/available_incremental_updates](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/available_incremental_updates.html)  | Given a set of hosts and errata, lists the content view versions and environments that need updating. |
| hosts.hosts_bulk_actions_bulk_add_host_collections | [PUT /api/hosts/bulk/add_host_collections](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/bulk_add_host_collections.html)  | Add one or more host collections to one or more hosts |
| hosts.hosts_bulk_actions_bulk_remove_host_collections | [PUT /api/hosts/bulk/remove_host_collections](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/bulk_remove_host_collections.html)  | Remove one or more host collections from one or more hosts |
| hosts.hosts_bulk_actions_content_overrides | [PUT /api/hosts/bulk/content_overrides](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/content_overrides.html)  | Set content overrides to one or more hosts |
| hosts.hosts_bulk_actions_destroy_hosts | [PUT /api/hosts/bulk/destroy](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/destroy_hosts.html)  | Destroy one or more hosts |
| hosts.hosts_bulk_actions_environment_content_view | [PUT /api/hosts/bulk/environment_content_view](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/environment_content_view.html)  | Assign the environment and content view to one or more hosts |
| hosts.hosts_bulk_actions_install_content | [PUT /api/hosts/bulk/install_content](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/install_content.html)  | Install content on one or more hosts |
| hosts.hosts_bulk_actions_installable_errata | [POST /api/hosts/bulk/installable_errata](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/installable_errata.html)  | Fetch installable errata for a host. |
| hosts.hosts_bulk_actions_module_streams | [POST /api/hosts/bulk/module_streams](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/module_streams.html)  | Fetch available module streams for hosts. |
| hosts.hosts_bulk_actions_release_version | [PUT /api/hosts/bulk/release_version](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/release_version.html)  | Assign the release version to one or more hosts |
| hosts.hosts_bulk_actions_remove_content | [PUT /api/hosts/bulk/remove_content](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/remove_content.html)  | Remove content on one or more hosts |
| hosts.hosts_bulk_actions_remove_subscriptions | [PUT /api/hosts/bulk/remove_subscriptions](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/remove_subscriptions.html)  | Remove subscriptions from one or more hosts |
| hosts.hosts_bulk_actions_update_content | [PUT /api/hosts/bulk/update_content](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/update_content.html)  | Update content on one or more hosts |
| hosts.id_get_statusstatus | [GET /api/hosts/:id/status/:type](https://theforeman.org/api/1.16/apidoc/v2/hosts/get_status.html)  | Get status of host |
| hosts.id_templatetemplate | [GET /api/hosts/:id/template/:kind](https://theforeman.org/api/1.16/apidoc/v2/hosts/template.html)  | Preview rendered provisioning template content |
| hosts.index | [GET /api/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/index.html)  | List all hosts |
| hosts.interfaces_create | [POST /api/hosts/:host_id/interfaces](https://theforeman.org/api/1.16/apidoc/v2/interfaces/create.html)  | Create an interface on a host |
| hosts.interfaces_host_id_destroyinterfaces | [DELETE /api/hosts/:host_id/interfaces/:id](https://theforeman.org/api/1.16/apidoc/v2/interfaces/destroy.html)  | Delete a host's interface |
| hosts.interfaces_host_id_showinterfaces | [GET /api/hosts/:host_id/interfaces/:id](https://theforeman.org/api/1.16/apidoc/v2/interfaces/show.html)  | Show an interface for host |
| hosts.interfaces_host_id_updateinterfaces | [PUT /api/hosts/:host_id/interfaces/:id](https://theforeman.org/api/1.16/apidoc/v2/interfaces/update.html)  | Update a host's interface |
| hosts.interfaces_index | [GET /api/hosts/:host_id/interfaces](https://theforeman.org/api/1.16/apidoc/v2/interfaces/index.html)  | List all interfaces for host |
| hosts.multiple_play_roles | [POST /api/hosts/multiple_play_roles](https://theforeman.org/api/1.16/apidoc/v2/hosts/multiple_play_roles.html)  | Runs all Ansible roles on hosts |
| hosts.parameters_create | [POST /api/hosts/:host_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for a host |
| hosts.parameters_host_id_destroyparameters | [DELETE /api/hosts/:host_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for a host |
| hosts.parameters_host_id_showparameters | [GET /api/hosts/:host_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for a host |
| hosts.parameters_host_id_updateparameters | [PUT /api/hosts/:host_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for a host |
| hosts.parameters_index | [GET /api/hosts/:host_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for a host |
| hosts.parameters_reset | [DELETE /api/hosts/:host_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameters for a host |
| hosts.play_roles | [POST /api/hosts/:id/play_roles](https://theforeman.org/api/1.16/apidoc/v2/hosts/play_roles.html)  | Runs all Ansible roles on a host |
| hosts.power | [PUT /api/hosts/:id/power](https://theforeman.org/api/1.16/apidoc/v2/hosts/power.html)  | Run a power operation on host |
| hosts.power_status | [GET /api/hosts/:id/power](https://theforeman.org/api/1.16/apidoc/v2/hosts/power_status.html)  | Fetch the status of whether the host is powered on or not. Supported hosts are VMs and physical hosts with BMCs. |
| hosts.puppet_hosts_puppetrun | [PUT /api/hosts/:id/puppetrun](https://theforeman.org/api/1.16/apidoc/v2/puppet_hosts/puppetrun.html)  | Force a Puppet agent run on the host |
| hosts.puppetclasses_host_id_showpuppetclasses | [GET /api/hosts/:host_id/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/show.html)  | Show a Puppet class for host |
| hosts.puppetclasses_index | [GET /api/hosts/:host_id/puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/index.html)  | List all Puppet classes for a host |
| hosts.rebuild_config | [PUT /api/hosts/:id/rebuild_config](https://theforeman.org/api/1.16/apidoc/v2/hosts/rebuild_config.html)  | Rebuild orchestration config |
| hosts.reports_last | [GET /api/hosts/:host_id/reports/last](https://theforeman.org/api/1.16/apidoc/v2/reports/last.html)  | Show the last report for a host |
| hosts.show | [GET /api/hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/hosts/show.html)  | Show a host |
| hosts.smart_class_parameters_index | [GET /api/hosts/:host_id/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List of smart class parameters for a specific host |
| hosts.smart_variables_index | [GET /api/hosts/:host_id/smart_variables](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/index.html)  | List of smart variables for a specific host |
| hosts.snapshots_create | [POST /api/hosts/:host_id/snapshots](https://theforeman.org/api/1.16/apidoc/v2/snapshots/create.html)  | Create a snapshot |
| hosts.snapshots_host_id_destroysnapshots | [DELETE /api/hosts/:host_id/snapshots/:id](https://theforeman.org/api/1.16/apidoc/v2/snapshots/destroy.html)  | Delete a snapshot |
| hosts.snapshots_host_id_revertsnapshots | [PUT /api/hosts/:host_id/snapshots/:id/revert](https://theforeman.org/api/1.16/apidoc/v2/snapshots/revert.html)  | Revert Host to a snapshot |
| hosts.snapshots_host_id_showsnapshots | [GET /api/hosts/:host_id/snapshots/:id](https://theforeman.org/api/1.16/apidoc/v2/snapshots/show.html)  | Show a snapshot |
| hosts.snapshots_host_id_updatesnapshots | [PUT /api/hosts/:host_id/snapshots/:id](https://theforeman.org/api/1.16/apidoc/v2/snapshots/update.html)  | Update a snapshot |
| hosts.snapshots_index | [GET /api/hosts/:host_id/snapshots](https://theforeman.org/api/1.16/apidoc/v2/snapshots/index.html)  | List all snapshots |
| hosts.status | [GET /api/hosts/:id/status](https://theforeman.org/api/1.16/apidoc/v2/hosts/status.html)  | Get configuration status of host |
| hosts.update | [PUT /api/hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/hosts/update.html)  | Update a host |
| hosts.vm_compute_attributes | [GET /api/hosts/:id/vm_compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/hosts/vm_compute_attributes.html)  | Get vm attributes of host |
| http_proxies.create | [POST /api/http_proxies](https://theforeman.org/api/1.16/apidoc/v2/http_proxies/create.html)  | Create an HTTP Proxy |
| http_proxies.destroy | [DELETE /api/http_proxies/:id](https://theforeman.org/api/1.16/apidoc/v2/http_proxies/destroy.html)  | Delete an HTTP Proxy |
| http_proxies.index | [GET /api/http_proxies](https://theforeman.org/api/1.16/apidoc/v2/http_proxies/index.html)  | List of HTTP Proxies |
| http_proxies.show | [GET /api/http_proxies/:id](https://theforeman.org/api/1.16/apidoc/v2/http_proxies/show.html)  | Show an HTTP Proxy |
| http_proxies.update | [PUT /api/http_proxies/:id](https://theforeman.org/api/1.16/apidoc/v2/http_proxies/update.html)  | Update an HTTP Proxy |
| job_invocations.cancel | [POST /api/job_invocations/:id/cancel](https://theforeman.org/api/1.16/apidoc/v2/job_invocations/cancel.html)  | Cancel job invocation |
| job_invocations.create | [POST /api/job_invocations](https://theforeman.org/api/1.16/apidoc/v2/job_invocations/create.html)  | Create a job invocation |
| job_invocations.id_outputhosts | [GET /api/job_invocations/:id/hosts/:host_id](https://theforeman.org/api/1.16/apidoc/v2/job_invocations/output.html)  | Get output for a host |
| job_invocations.id_raw_outputhosts | [GET /api/job_invocations/:id/hosts/:host_id/raw](https://theforeman.org/api/1.16/apidoc/v2/job_invocations/raw_output.html)  | Get raw output for a host |
| job_invocations.index | [GET /api/job_invocations](https://theforeman.org/api/1.16/apidoc/v2/job_invocations/index.html)  | List job invocations |
| job_invocations.rerun | [POST /api/job_invocations/:id/rerun](https://theforeman.org/api/1.16/apidoc/v2/job_invocations/rerun.html)  | Rerun job on failed hosts |
| job_invocations.show | [GET /api/job_invocations/:id](https://theforeman.org/api/1.16/apidoc/v2/job_invocations/show.html)  | Show job invocation |
| job_invocations.template_invocations_template_invocations | [GET /api/job_invocations/:job_invocation_id/template_invocations](https://theforeman.org/api/1.16/apidoc/v2/template_invocations/template_invocations.html)  | List template invocations belonging to job invocation |
| job_templates.clone | [POST /api/job_templates/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/job_templates/clone.html)  | Clone a provision template |
| job_templates.create | [POST /api/job_templates](https://theforeman.org/api/1.16/apidoc/v2/job_templates/create.html)  | Create a job template |
| job_templates.destroy | [DELETE /api/job_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/job_templates/destroy.html)  | Delete a job template |
| job_templates.export | [GET /api/job_templates/:id/export](https://theforeman.org/api/1.16/apidoc/v2/job_templates/export.html)  | Export a job template to ERB |
| job_templates.import_ | [POST /api/job_templates/import](https://theforeman.org/api/1.16/apidoc/v2/job_templates/import.html)  | Import a job template from ERB |
| job_templates.index | [GET /api/job_templates](https://theforeman.org/api/1.16/apidoc/v2/job_templates/index.html)  | List job templates |
| job_templates.revision | [GET /api/job_templates/revision](https://theforeman.org/api/1.16/apidoc/v2/job_templates/revision.html)  |  |
| job_templates.show | [GET /api/job_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/job_templates/show.html)  | Show job template details |
| job_templates.update | [PUT /api/job_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/job_templates/update.html)  | Update a job template |
| locations.auth_source_externals_index | [GET /api/locations/:location_id/auth_source_externals](https://theforeman.org/api/1.16/apidoc/v2/auth_source_externals/index.html)  | List external authentication sources per location |
| locations.auth_source_ldaps_index | [GET /api/locations/:location_id/auth_source_ldaps](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/index.html)  | List LDAP authentication sources per location |
| locations.auth_sources_index | [GET /api/locations/:location_id/auth_sources](https://theforeman.org/api/1.16/apidoc/v2/auth_sources/index.html)  | List all authentication sources per location |
| locations.config_templates_index | [GET /api/locations/:location_id/config_templates](https://theforeman.org/api/1.16/apidoc/v2/config_templates/index.html)  | List provisioning templates per location |
| locations.create | [POST /api/locations](https://theforeman.org/api/1.16/apidoc/v2/locations/create.html)  | Create a location |
| locations.destroy | [DELETE /api/locations/:id](https://theforeman.org/api/1.16/apidoc/v2/locations/destroy.html)  | Delete a location |
| locations.domains_index | [GET /api/locations/:location_id/domains](https://theforeman.org/api/1.16/apidoc/v2/domains/index.html)  | List of domains per location |
| locations.environments_index | [GET /api/locations/:location_id/environments](https://theforeman.org/api/1.16/apidoc/v2/environments/index.html)  | List environments per location |
| locations.hostgroups_index | [GET /api/locations/:location_id/hostgroups](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/index.html)  | List all host groups per location |
| locations.hosts_index | [GET /api/locations/:location_id/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/index.html)  | List hosts per location |
| locations.index | [GET /api/locations](https://theforeman.org/api/1.16/apidoc/v2/locations/index.html)  | List all locations |
| locations.job_templates_index | [GET /api/locations/:location_id/job_templates](https://theforeman.org/api/1.16/apidoc/v2/job_templates/index.html)  | List job templates per location |
| locations.media_index | [GET /api/locations/:location_id/media](https://theforeman.org/api/1.16/apidoc/v2/media/index.html)  | List all media per location |
| locations.parameters_create | [POST /api/locations/:location_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for a location |
| locations.parameters_index | [GET /api/locations/:location_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for a location |
| locations.parameters_location_id_destroyparameters | [DELETE /api/locations/:location_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for a location |
| locations.parameters_location_id_showparameters | [GET /api/locations/:location_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for a location |
| locations.parameters_location_id_updateparameters | [PUT /api/locations/:location_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for a location |
| locations.parameters_reset | [DELETE /api/locations/:location_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameter for a location |
| locations.provisioning_templates_index | [GET /api/locations/:location_id/provisioning_templates](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/index.html)  | List provisioning templates per location |
| locations.ptables_index | [GET /api/locations/:location_id/ptables](https://theforeman.org/api/1.16/apidoc/v2/ptables/index.html)  | List all partition tables per location |
| locations.report_templates_index | [GET /api/locations/:location_id/report_templates](https://theforeman.org/api/1.16/apidoc/v2/report_templates/index.html)  | List all report templates per location |
| locations.show | [GET /api/locations/:id](https://theforeman.org/api/1.16/apidoc/v2/locations/show.html)  | Show a location |
| locations.subnets_index | [GET /api/locations/:location_id/subnets](https://theforeman.org/api/1.16/apidoc/v2/subnets/index.html)  | List of subnets per location |
| locations.update | [PUT /api/locations/:id](https://theforeman.org/api/1.16/apidoc/v2/locations/update.html)  | Update a location |
| locations.users_index | [GET /api/locations/:location_id/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users for location |
| mail_notifications.index | [GET /api/mail_notifications](https://theforeman.org/api/1.16/apidoc/v2/mail_notifications/index.html)  | List of email notifications |
| mail_notifications.show | [GET /api/mail_notifications/:id](https://theforeman.org/api/1.16/apidoc/v2/mail_notifications/show.html)  | Show an email notification |
| media.create | [POST /api/media](https://theforeman.org/api/1.16/apidoc/v2/media/create.html)  | Create a medium |
| media.destroy | [DELETE /api/media/:id](https://theforeman.org/api/1.16/apidoc/v2/media/destroy.html)  | Delete a medium |
| media.index | [GET /api/media](https://theforeman.org/api/1.16/apidoc/v2/media/index.html)  | List all installation media |
| media.operatingsystems_index | [GET /api/media/:medium_id/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems for nested medium |
| media.show | [GET /api/media/:id](https://theforeman.org/api/1.16/apidoc/v2/media/show.html)  | Show a medium |
| media.update | [PUT /api/media/:id](https://theforeman.org/api/1.16/apidoc/v2/media/update.html)  | Update a medium |
| models.create | [POST /api/models](https://theforeman.org/api/1.16/apidoc/v2/models/create.html)  | Create a hardware model |
| models.destroy | [DELETE /api/models/:id](https://theforeman.org/api/1.16/apidoc/v2/models/destroy.html)  | Delete a hardware model |
| models.index | [GET /api/models](https://theforeman.org/api/1.16/apidoc/v2/models/index.html)  | List all hardware models |
| models.show | [GET /api/models/:id](https://theforeman.org/api/1.16/apidoc/v2/models/show.html)  | Show a hardware model |
| models.update | [PUT /api/models/:id](https://theforeman.org/api/1.16/apidoc/v2/models/update.html)  | Update a hardware model |
| module_streams.compare | [GET /katello/api/module_streams/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/module_streams/compare.html)  | List module_streams |
| module_streams.index | [GET /katello/api/module_streams](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/module_streams/index.html)  | List module_streams |
| module_streams.show | [GET /katello/api/module_streams/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/module_streams/show.html)  | Show a module stream |
| operatingsystems.architectures_index | [GET /api/operatingsystems/:operatingsystem_id/architectures](https://theforeman.org/api/1.16/apidoc/v2/architectures/index.html)  | List all architectures for operating system |
| operatingsystems.bootfiles | [GET /api/operatingsystems/:id/bootfiles](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/bootfiles.html)  | List boot files for an operating system |
| operatingsystems.config_templates_index | [GET /api/operatingsystems/:operatingsystem_id/config_templates](https://theforeman.org/api/1.16/apidoc/v2/config_templates/index.html)  | List provisioning templates per operating system |
| operatingsystems.create | [POST /api/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/create.html)  | Create an operating system |
| operatingsystems.destroy | [DELETE /api/operatingsystems/:id](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/destroy.html)  | Delete an operating system |
| operatingsystems.images_index | [GET /api/operatingsystems/:operatingsystem_id/images](https://theforeman.org/api/1.16/apidoc/v2/images/index.html)  | List all images for operating system |
| operatingsystems.images_operatingsystem_id_showimages | [GET /api/operatingsystems/:operatingsystem_id/images/:id](https://theforeman.org/api/1.16/apidoc/v2/images/show.html)  | Show an image |
| operatingsystems.index | [GET /api/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems |
| operatingsystems.media_index | [GET /api/operatingsystems/:operatingsystem_id/media](https://theforeman.org/api/1.16/apidoc/v2/media/index.html)  | List all media for an operating system |
| operatingsystems.os_default_templates_create | [POST /api/operatingsystems/:operatingsystem_id/os_default_templates](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/create.html)  | Create a default template combination for an operating system |
| operatingsystems.os_default_templates_index | [GET /api/operatingsystems/:operatingsystem_id/os_default_templates](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/index.html)  | List default templates combinations for an operating system |
| operatingsystems.os_default_templates_operatingsystem_id_os_default_destroytemplates | [DELETE /api/operatingsystems/:operatingsystem_id/os_default_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/destroy.html)  | Delete a default template combination for an operating system |
| operatingsystems.os_default_templates_operatingsystem_id_os_default_showtemplates | [GET /api/operatingsystems/:operatingsystem_id/os_default_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/show.html)  | Show a default template combination for an operating system |
| operatingsystems.os_default_templates_operatingsystem_id_os_default_updatetemplates | [PUT /api/operatingsystems/:operatingsystem_id/os_default_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/update.html)  | Update a default template combination for an operating system |
| operatingsystems.parameters_create | [POST /api/operatingsystems/:operatingsystem_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for an operating system |
| operatingsystems.parameters_index | [GET /api/operatingsystems/:operatingsystem_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for an operating system |
| operatingsystems.parameters_operatingsystem_id_destroyparameters | [DELETE /api/operatingsystems/:operatingsystem_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for an operating system |
| operatingsystems.parameters_operatingsystem_id_showparameters | [GET /api/operatingsystems/:operatingsystem_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for an operating system |
| operatingsystems.parameters_operatingsystem_id_updateparameters | [PUT /api/operatingsystems/:operatingsystem_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for an operating system |
| operatingsystems.parameters_reset | [DELETE /api/operatingsystems/:operatingsystem_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameters for an operating system |
| operatingsystems.provisioning_templates_index | [GET /api/operatingsystems/:operatingsystem_id/provisioning_templates](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/index.html)  | List provisioning templates per operating system |
| operatingsystems.ptables_index | [GET /api/operatingsystems/:operatingsystem_id/ptables](https://theforeman.org/api/1.16/apidoc/v2/ptables/index.html)  | List all partition tables for an operating system |
| operatingsystems.show | [GET /api/operatingsystems/:id](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/show.html)  | Show an operating system |
| operatingsystems.update | [PUT /api/operatingsystems/:id](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/update.html)  | Update an operating system |
| orchestration.tasks_index | [GET /api/orchestration/:id/tasks](https://theforeman.org/api/1.16/apidoc/v2/tasks/index.html)  | List all tasks for a given orchestration event |
| organizations.activation_keys_index | [GET /katello/api/organizations/:organization_id/activation_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/index.html)  |  |
| organizations.auth_source_externals_index | [GET /api/organizations/:organization_id/auth_source_externals](https://theforeman.org/api/1.16/apidoc/v2/auth_source_externals/index.html)  | List external authentication sources per organization |
| organizations.auth_source_ldaps_index | [GET /api/organizations/:organization_id/auth_source_ldaps](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/index.html)  | List LDAP authentication sources per organization |
| organizations.auth_sources_index | [GET /api/organizations/:organization_id/auth_sources](https://theforeman.org/api/1.16/apidoc/v2/auth_sources/index.html)  | List all authentication sources per organization |
| organizations.autoattach_subscriptions | [POST /katello/api/organizations/:id/autoattach_subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/autoattach_subscriptions.html)  | Auto-attach available subscriptions to all hosts within an organization. Asynchronous operation. |
| organizations.cancel_repo_discover | [PUT /katello/api/organizations/:label/cancel_repo_discover](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/cancel_repo_discover.html)  | Cancel repository discovery |
| organizations.config_templates_index | [GET /api/organizations/:organization_id/config_templates](https://theforeman.org/api/1.16/apidoc/v2/config_templates/index.html)  | List provisioning templates per organization |
| organizations.content_views_create | [POST /katello/api/organizations/:organization_id/content_views](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/create.html)  | Create a content view |
| organizations.content_views_index | [GET /katello/api/organizations/:organization_id/content_views](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/index.html)  | List content views |
| organizations.create | [POST /katello/api/organizations](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/create.html)  | Create organization |
| organizations.destroy | [DELETE /katello/api/organizations/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/destroy.html)  | Delete an organization |
| organizations.domains_index | [GET /api/organizations/:organization_id/domains](https://theforeman.org/api/1.16/apidoc/v2/domains/index.html)  | List of domains per organization |
| organizations.download_debug_certificate | [GET /katello/api/organizations/:label/download_debug_certificate](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/download_debug_certificate.html)  | Download a debug certificate |
| organizations.environments_index | [GET /api/organizations/:organization_id/environments](https://theforeman.org/api/1.16/apidoc/v2/environments/index.html)  | List environments per organization |
| organizations.host_collections_create | [POST /katello/api/organizations/:organization_id/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/create.html)  | Create a host collection |
| organizations.host_collections_index | [GET /katello/api/organizations/:organization_id/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/index.html)  | List host collections within an organization |
| organizations.hostgroups_index | [GET /api/organizations/:organization_id/hostgroups](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/index.html)  | List all host groups per organization |
| organizations.hosts_index | [GET /api/organizations/:organization_id/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/index.html)  | List hosts per organization |
| organizations.index | [GET /katello/api/organizations](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/index.html)  | List all organizations |
| organizations.job_templates_index | [GET /api/organizations/:organization_id/job_templates](https://theforeman.org/api/1.16/apidoc/v2/job_templates/index.html)  | List job templates per organization |
| organizations.lifecycle_environments_create | [POST /katello/api/organizations/:organization_id/environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/create.html)  | Create an environment in an organization |
| organizations.lifecycle_environments_index | [GET /katello/api/organizations/:organization_id/environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/index.html)  | List environments in an organization |
| organizations.lifecycle_environments_paths | [GET /katello/api/organizations/:organization_id/environments/paths](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/paths.html)  | List environment paths |
| organizations.lifecycle_environments_rganizations | [GET /katello/api/organizations/:organization_id/environments/:environment_id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/show.html)  | Show an environment |
| organizations.media_index | [GET /api/organizations/:organization_id/media](https://theforeman.org/api/1.16/apidoc/v2/media/index.html)  | List all media per organization |
| organizations.parameters_create | [POST /api/organizations/:organization_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for an organization |
| organizations.parameters_index | [GET /api/organizations/:organization_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for an organization |
| organizations.parameters_organization_id_destroyparameters | [DELETE /api/organizations/:organization_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for an organization |
| organizations.parameters_organization_id_showparameters | [GET /api/organizations/:organization_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for an organization |
| organizations.parameters_organization_id_updateparameters | [PUT /api/organizations/:organization_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for an organization |
| organizations.parameters_reset | [DELETE /api/organizations/:organization_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameter for an organization |
| organizations.products_index | [GET /katello/api/organizations/:organization_id/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List of products in an organization |
| organizations.products_rganizations | [GET /katello/api/organizations/:organization_id/sync_plans/:sync_plan_id/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List of Products for sync plan |
| organizations.provisioning_templates_index | [GET /api/organizations/:organization_id/provisioning_templates](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/index.html)  | List provisioning templates per organization |
| organizations.ptables_index | [GET /api/organizations/:organization_id/ptables](https://theforeman.org/api/1.16/apidoc/v2/ptables/index.html)  | List all partition tables per organization |
| organizations.redhat_provider | [GET /katello/api/organizations/:id/redhat_provider](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/redhat_provider.html)  | List all :resource_id |
| organizations.releases | [GET /katello/api/organizations/:id/releases](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/releases.html)  | List available releases in the organization |
| organizations.repo_discover | [PUT /katello/api/organizations/:id/repo_discover](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/repo_discover.html)  | Discover Repositories |
| organizations.report_templates_index | [GET /api/organizations/:organization_id/report_templates](https://theforeman.org/api/1.16/apidoc/v2/report_templates/index.html)  | List all report templates per organization |
| organizations.repositories_index | [GET /katello/api/organizations/:organization_id/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/index.html)  | List of repositories in an organization |
| organizations.repositories_rganizations | [GET /katello/api/organizations/:organization_id/environments/:environment_id/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/index.html)  | List repositories in the environment |
| organizations.show | [GET /katello/api/organizations/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/show.html)  | Show organization |
| organizations.subnets_index | [GET /api/organizations/:organization_id/subnets](https://theforeman.org/api/1.16/apidoc/v2/subnets/index.html)  | List of subnets per organization |
| organizations.subscriptions_delete_manifest | [POST /katello/api/organizations/:organization_id/subscriptions/delete_manifest](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/delete_manifest.html)  | Delete manifest from Red Hat provider |
| organizations.subscriptions_index | [GET /katello/api/organizations/:organization_id/subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/index.html)  | List organization subscriptions |
| organizations.subscriptions_manifest_history | [GET /katello/api/organizations/:organization_id/subscriptions/manifest_history](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/manifest_history.html)  | obtain manifest history for subscriptions |
| organizations.subscriptions_refresh_manifest | [PUT /katello/api/organizations/:organization_id/subscriptions/refresh_manifest](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/refresh_manifest.html)  | Refresh previously imported manifest for Red Hat provider |
| organizations.subscriptions_rganizations | [GET /katello/api/organizations/:organization_id/subscriptions/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/show.html)  | Show a subscription |
| organizations.subscriptions_upload | [POST /katello/api/organizations/:organization_id/subscriptions/upload](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/upload.html)  | Upload a subscription manifest |
| organizations.sync_plans_create | [POST /katello/api/organizations/:organization_id/sync_plans](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/create.html)  | Create a sync plan |
| organizations.sync_plans_index | [GET /katello/api/organizations/:organization_id/sync_plans](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/index.html)  |  |
| organizations.sync_plans_rganizations | [GET /katello/api/organizations/:organization_id/sync_plans/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/show.html)  | Show a sync plan |
| organizations.sync_rganizations | [GET /katello/api/organizations/:organization_id/products/:product_id/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync/index.html)  | Get status of repo synchronisation for given product |
| organizations.update | [PUT /katello/api/organizations/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/update.html)  | Update organization |
| organizations.upstream_subscriptions_create | [POST /katello/api/organizations/:organization_id/upstream_subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/upstream_subscriptions/create.html)  | Add subscriptions consumed by a manifest from Red Hat Subscription Management |
| organizations.upstream_subscriptions_destroy | [DELETE /katello/api/organizations/:organization_id/upstream_subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/upstream_subscriptions/destroy.html)  | Remove one or more subscriptions from an upstream subscription allocation |
| organizations.upstream_subscriptions_index | [GET /katello/api/organizations/:organization_id/upstream_subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/upstream_subscriptions/index.html)  | List available subscriptions from Red Hat Subscription Management |
| organizations.upstream_subscriptions_update | [PUT /katello/api/organizations/:organization_id/upstream_subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/upstream_subscriptions/update.html)  | Update the quantity of one or more subscriptions on an upstream allocation |
| organizations.users_index | [GET /api/organizations/:organization_id/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users for organization |
| ostree_branches.compare | [GET /katello/api/ostree_branches/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/compare.html)  | List ostree_branches |
| ostree_branches.index | [GET /katello/api/ostree_branches](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/index.html)  | List ostree_branches |
| ostree_branches.show | [GET /katello/api/ostree_branches/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/show.html)  | Show an ostree branch |
| package_group.package_groups_create | [POST /katello/api/package_group](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/create.html)  | Create a package group |
| package_group.package_groups_destroy | [DELETE /katello/api/package_group](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/destroy.html)  | Delete a package group |
| package_groups.compare | [GET /katello/api/package_groups/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/compare.html)  | List package_groups |
| package_groups.index | [GET /katello/api/package_groups](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/index.html)  | List package_groups |
| package_groups.show | [GET /katello/api/package_groups/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/show.html)  | Show a package group |
| packages.compare | [GET /katello/api/packages/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/compare.html)  | List packages |
| packages.index | [GET /katello/api/packages](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/index.html)  | List packages |
| packages.show | [GET /katello/api/packages/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/show.html)  | Show a package |
| permissions.index | [GET /api/permissions](https://theforeman.org/api/1.16/apidoc/v2/permissions/index.html)  | List all permissions |
| permissions.resource_types | [GET /api/permissions/resource_types](https://theforeman.org/api/1.16/apidoc/v2/permissions/resource_types.html)  | List available resource types |
| permissions.show | [GET /api/permissions/:id](https://theforeman.org/api/1.16/apidoc/v2/permissions/show.html)  | Show a permission |
| ping.index | [GET /katello/api/ping](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ping/index.html)  | Shows status of orcharhino system and it's subcomponents |
| ping.ping | [GET /api/ping](https://theforeman.org/api/1.16/apidoc/v2/ping/ping.html)  | Shows status of orcharhino system and it's subcomponents |
| products.create | [POST /katello/api/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/create.html)  | Create a product |
| products.destroy | [DELETE /katello/api/products/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/destroy.html)  | Destroy a product |
| products.index | [GET /katello/api/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List products |
| products.products_bulk_actions_destroy_products | [PUT /katello/api/products/bulk/destroy](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products_bulk_actions/destroy_products.html)  | Destroy one or more products |
| products.products_bulk_actions_sync_products | [PUT /katello/api/products/bulk/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products_bulk_actions/sync_products.html)  | Sync one or more products |
| products.products_bulk_actions_update_http_proxy | [PUT /katello/api/products/bulk/http_proxy](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products_bulk_actions/update_http_proxy.html)  | Update the http proxy configuration on the repositories of one or more products. |
| products.products_bulk_actions_update_sync_plans | [PUT /katello/api/products/bulk/sync_plan](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products_bulk_actions/update_sync_plans.html)  | Sync one or more products |
| products.repositories_index | [GET /katello/api/products/:product_id/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/index.html)  | List of repositories for a product |
| products.repository_sets_index | [GET /katello/api/products/:product_id/repository_sets](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repository_sets/index.html)  | List repository sets for a product. |
| products.repository_sets_roducts | [GET /katello/api/products/:product_id/repository_sets/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repository_sets/show.html)  | Get info about a repository set |
| products.show | [GET /katello/api/products/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/show.html)  | Show a product |
| products.sync | [POST /katello/api/products/:id/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/sync.html)  | Sync all repositories for a product |
| products.update | [PUT /katello/api/products/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/update.html)  | Updates a product |
| provisioning_templates.build_pxe_default | [POST /api/provisioning_templates/build_pxe_default](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/build_pxe_default.html)  | Update the default PXE menu on all configured TFTP servers |
| provisioning_templates.clone | [POST /api/provisioning_templates/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/clone.html)  | Clone a provision template |
| provisioning_templates.create | [POST /api/provisioning_templates](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/create.html)  | Create a provisioning template |
| provisioning_templates.destroy | [DELETE /api/provisioning_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/destroy.html)  | Delete a provisioning template |
| provisioning_templates.export | [GET /api/provisioning_templates/:id/export](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/export.html)  | Export a provisioning template to ERB |
| provisioning_templates.import_ | [POST /api/provisioning_templates/import](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/import.html)  | Import a provisioning template |
| provisioning_templates.index | [GET /api/provisioning_templates](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/index.html)  | List provisioning templates |
| provisioning_templates.operatingsystems_index | [GET /api/provisioning_templates/:provisioning_template_id/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems for nested provisioning template |
| provisioning_templates.os_default_templates_index | [GET /api/provisioning_templates/:provisioning_template_id/os_default_templates](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/index.html)  | List operating systems where this template is set as a default |
| provisioning_templates.revision | [GET /api/provisioning_templates/revision](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/revision.html)  |  |
| provisioning_templates.show | [GET /api/provisioning_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/show.html)  | Show provisioning template details |
| provisioning_templates.template_combinations_create | [POST /api/provisioning_templates/:provisioning_template_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/create.html)  | Add a template combination |
| provisioning_templates.template_combinations_index | [GET /api/provisioning_templates/:provisioning_template_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/index.html)  | List template combination |
| provisioning_templates.template_combinations_provisioning_template_id_template_showcombinations | [GET /api/provisioning_templates/:provisioning_template_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/show.html)  | Show template combination |
| provisioning_templates.template_combinations_provisioning_template_id_template_updatecombinations | [PUT /api/provisioning_templates/:provisioning_template_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/update.html)  | Update template combination |
| provisioning_templates.update | [PUT /api/provisioning_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/update.html)  | Update a provisioning template |
| ptables.clone | [POST /api/ptables/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/ptables/clone.html)  | Clone a template |
| ptables.create | [POST /api/ptables](https://theforeman.org/api/1.16/apidoc/v2/ptables/create.html)  | Create a partition table |
| ptables.destroy | [DELETE /api/ptables/:id](https://theforeman.org/api/1.16/apidoc/v2/ptables/destroy.html)  | Delete a partition table |
| ptables.export | [GET /api/ptables/:id/export](https://theforeman.org/api/1.16/apidoc/v2/ptables/export.html)  | Export a partition template to ERB |
| ptables.import_ | [POST /api/ptables/import](https://theforeman.org/api/1.16/apidoc/v2/ptables/import.html)  | Import a provisioning template |
| ptables.index | [GET /api/ptables](https://theforeman.org/api/1.16/apidoc/v2/ptables/index.html)  | List all partition tables |
| ptables.operatingsystems_index | [GET /api/ptables/:ptable_id/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems for nested partition table |
| ptables.revision | [GET /api/ptables/revision](https://theforeman.org/api/1.16/apidoc/v2/ptables/revision.html)  |  |
| ptables.show | [GET /api/ptables/:id](https://theforeman.org/api/1.16/apidoc/v2/ptables/show.html)  | Show a partition table |
| ptables.update | [PUT /api/ptables/:id](https://theforeman.org/api/1.16/apidoc/v2/ptables/update.html)  | Update a partition table |
| puppet_modules.compare | [GET /katello/api/puppet_modules/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/compare.html)  | List puppet_modules |
| puppet_modules.index | [GET /katello/api/puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/index.html)  | List puppet_modules |
| puppet_modules.show | [GET /katello/api/puppet_modules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/show.html)  | Show a puppet module |
| puppetclasses.create | [POST /api/puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/create.html)  | Create a Puppet class |
| puppetclasses.destroy | [DELETE /api/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/destroy.html)  | Delete a Puppet class |
| puppetclasses.environments_index | [GET /api/puppetclasses/:puppetclass_id/environments](https://theforeman.org/api/1.16/apidoc/v2/environments/index.html)  | List environments of Puppet class |
| puppetclasses.hostgroups_index | [GET /api/puppetclasses/:puppetclass_id/hostgroups](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/index.html)  | List all host groups for a Puppet class |
| puppetclasses.index | [GET /api/puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/index.html)  | List all Puppet classes |
| puppetclasses.show | [GET /api/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/show.html)  | Show a Puppet class |
| puppetclasses.smart_class_parameters_index | [GET /api/puppetclasses/:puppetclass_id/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List of smart class parameters for a specific Puppet class |
| puppetclasses.smart_variables_index | [GET /api/puppetclasses/:puppetclass_id/smart_variables](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/index.html)  | List of smart variables for a specific Puppet class |
| puppetclasses.update | [PUT /api/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/update.html)  | Update a Puppet class |
| realms.create | [POST /api/realms](https://theforeman.org/api/1.16/apidoc/v2/realms/create.html)  | Create a realm |
| realms.destroy | [DELETE /api/realms/:id](https://theforeman.org/api/1.16/apidoc/v2/realms/destroy.html)  | Delete a realm |
| realms.index | [GET /api/realms](https://theforeman.org/api/1.16/apidoc/v2/realms/index.html)  | List of realms |
| realms.show | [GET /api/realms/:id](https://theforeman.org/api/1.16/apidoc/v2/realms/show.html)  | Show a realm |
| realms.update | [PUT /api/realms/:id](https://theforeman.org/api/1.16/apidoc/v2/realms/update.html)  | Update a realm |
| remote_execution_features.index | [GET /api/remote_execution_features](https://theforeman.org/api/1.16/apidoc/v2/remote_execution_features/index.html)  | List remote execution features |
| remote_execution_features.show | [GET /api/remote_execution_features/:id](https://theforeman.org/api/1.16/apidoc/v2/remote_execution_features/show.html)  | Show remote execution feature |
| remote_execution_features.update | [PUT /api/remote_execution_features/:id](https://theforeman.org/api/1.16/apidoc/v2/remote_execution_features/update.html)  | Update a job template |
| report_templates.clone | [POST /api/report_templates/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/report_templates/clone.html)  | Clone a template |
| report_templates.create | [POST /api/report_templates](https://theforeman.org/api/1.16/apidoc/v2/report_templates/create.html)  | Create a report template |
| report_templates.destroy | [DELETE /api/report_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/report_templates/destroy.html)  | Delete a report template |
| report_templates.export | [GET /api/report_templates/:id/export](https://theforeman.org/api/1.16/apidoc/v2/report_templates/export.html)  | Export a report template to ERB |
| report_templates.generate | [POST /api/report_templates/:id/generate](https://theforeman.org/api/1.16/apidoc/v2/report_templates/generate.html)  | Generate report from a template |
| report_templates.id_report_report_datadata | [GET /api/report_templates/:id/report_data/:job_id](https://theforeman.org/api/1.16/apidoc/v2/report_templates/report_data.html)  | Downloads a generated report |
| report_templates.import_ | [POST /api/report_templates/import](https://theforeman.org/api/1.16/apidoc/v2/report_templates/import.html)  | Import a report template |
| report_templates.index | [GET /api/report_templates](https://theforeman.org/api/1.16/apidoc/v2/report_templates/index.html)  | List all report templates |
| report_templates.revision | [GET /api/report_templates/revision](https://theforeman.org/api/1.16/apidoc/v2/report_templates/revision.html)  |  |
| report_templates.schedule_report | [POST /api/report_templates/:id/schedule_report](https://theforeman.org/api/1.16/apidoc/v2/report_templates/schedule_report.html)  | Schedule generating of a report |
| report_templates.show | [GET /api/report_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/report_templates/show.html)  | Show a report template |
| report_templates.update | [PUT /api/report_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/report_templates/update.html)  | Update a report template |
| reports.create | [POST /api/reports](https://theforeman.org/api/1.16/apidoc/v2/reports/create.html)  | Create a report |
| reports.destroy | [DELETE /api/reports/:id](https://theforeman.org/api/1.16/apidoc/v2/reports/destroy.html)  | Delete a report |
| reports.index | [GET /api/reports](https://theforeman.org/api/1.16/apidoc/v2/reports/index.html)  | List all reports |
| reports.show | [GET /api/reports/:id](https://theforeman.org/api/1.16/apidoc/v2/reports/show.html)  | Show a report |
| repositories.ansible_collections_epositories | [GET /katello/api/repositories/:repository_id/ansible_collections/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ansible_collections/show.html)  | Show an ansible collection |
| repositories.ansible_collections_index | [GET /katello/api/repositories/:repository_id/ansible_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ansible_collections/index.html)  | List ansible_collections |
| repositories.content_uploads_create | [POST /katello/api/repositories/:repository_id/content_uploads](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_uploads/create.html)  | Create an upload request |
| repositories.content_uploads_epositories | [PUT /katello/api/repositories/:repository_id/content_uploads/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_uploads/update.html)  | Upload a chunk of the file's content |
| repositories.create | [POST /katello/api/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/create.html)  | Create a custom repository |
| repositories.debs_epositories | [GET /katello/api/repositories/:repository_id/debs/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/debs/show.html)  | Show a deb package |
| repositories.debs_index | [GET /katello/api/repositories/:repository_id/debs](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/debs/index.html)  | List deb packages |
| repositories.destroy | [DELETE /katello/api/repositories/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/destroy.html)  | Destroy a custom repository |
| repositories.docker_manifest_lists_epositories | [GET /katello/api/repositories/:repository_id/docker_manifest_lists/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifest_lists/show.html)  | Show a docker manifest list |
| repositories.docker_manifest_lists_index | [GET /katello/api/repositories/:repository_id/docker_manifest_lists](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifest_lists/index.html)  | List docker_manifest_lists |
| repositories.docker_manifests_epositories | [GET /katello/api/repositories/:repository_id/docker_manifests/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/show.html)  | Show a docker manifest |
| repositories.docker_manifests_index | [GET /katello/api/repositories/:repository_id/docker_manifests](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/index.html)  | List docker_manifests |
| repositories.docker_tags_epositories | [GET /katello/api/repositories/:repository_id/docker_tags/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/show.html)  | Show a docker tag |
| repositories.docker_tags_index | [GET /katello/api/repositories/:repository_id/docker_tags](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/index.html)  | List docker_tags |
| repositories.errata_epositories | [GET /katello/api/repositories/:repository_id/errata/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/errata/show.html)  | Show an erratum |
| repositories.export | [POST /katello/api/repositories/:id/export](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/export.html)  | Export a repository |
| repositories.file_units_epositories | [GET /katello/api/repositories/:repository_id/files/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/file_units/show.html)  | Show a file |
| repositories.file_units_index | [GET /katello/api/repositories/:repository_id/files](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/file_units/index.html)  | List files |
| repositories.gpg_key_content | [GET /katello/api/repositories/:id/gpg_key_content](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/gpg_key_content.html)  | Return the content of a repo gpg key, used directly by yum |
| repositories.import_uploads | [PUT /katello/api/repositories/:id/import_uploads](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/import_uploads.html)  | Import uploads into a repository |
| repositories.index | [GET /katello/api/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/index.html)  | List of enabled repositories |
| repositories.module_streams_epositories | [GET /katello/api/repositories/:repository_id/module_streams/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/module_streams/show.html)  | Show a module stream |
| repositories.module_streams_index | [GET /katello/api/repositories/:repository_id/module_streams](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/module_streams/index.html)  | List module_streams |
| repositories.ostree_branches_epositories | [GET /katello/api/repositories/:repository_id/ostree_branches/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/show.html)  | Show an ostree branch |
| repositories.ostree_branches_index | [GET /katello/api/repositories/:repository_id/ostree_branches](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/index.html)  | List ostree_branches |
| repositories.package_groups_epositories | [GET /katello/api/repositories/:repository_id/package_groups/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/show.html)  | Show a package group |
| repositories.package_groups_index | [GET /katello/api/repositories/:repository_id/package_groups](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/index.html)  | List package_groups |
| repositories.packages_epositories | [GET /katello/api/repositories/:repository_id/:resource_id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/index.html)  | List :resource_id |
| repositories.puppet_modules_epositories | [GET /katello/api/repositories/:repository_id/puppet_modules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/show.html)  | Show a puppet module |
| repositories.puppet_modules_index | [GET /katello/api/repositories/:repository_id/puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/index.html)  | List puppet_modules |
| repositories.remove_content | [PUT /katello/api/repositories/:id/remove_packages](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/remove_content.html)  |  |
| repositories.repositories_bulk_actions_destroy_repositories | [PUT /katello/api/repositories/bulk/destroy](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories_bulk_actions/destroy_repositories.html)  | Destroy one or more repositories |
| repositories.repositories_bulk_actions_sync_repositories | [POST /katello/api/repositories/bulk/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories_bulk_actions/sync_repositories.html)  | Synchronize repository |
| repositories.repository_types | [GET /katello/api/repositories/repository_types](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/repository_types.html)  | Show the available repository types |
| repositories.republish | [PUT /katello/api/repositories/:id/republish](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/republish.html)  | Forces a republish of the specified repository, regenerating metadata and symlinks on the filesystem. |
| repositories.show | [GET /katello/api/repositories/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/show.html)  | Show a repository |
| repositories.srpms_epositories | [GET /katello/api/repositories/:repository_id/srpms/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/srpms/show.html)  | Show SRPM details |
| repositories.sync | [POST /katello/api/repositories/:id/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/sync.html)  | Sync a repository |
| repositories.sync_index | [GET /katello/api/repositories/:repository_id/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync/index.html)  | Get status of synchronisation for given repository |
| repositories.update | [PUT /katello/api/repositories/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/update.html)  | Update a repository |
| repositories.upload_content | [POST /katello/api/repositories/:id/upload_content](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/upload_content.html)  | Upload content into the repository |
| repository_sets.available_repositories | [GET /katello/api/repository_sets/:id/available_repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repository_sets/available_repositories.html)  | Get list of available repositories for the repository set |
| repository_sets.disable | [PUT /katello/api/repository_sets/:id/disable](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repository_sets/disable.html)  | Disable a repository from the set |
| repository_sets.enable | [PUT /katello/api/repository_sets/:id/enable](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repository_sets/enable.html)  | Enable a repository from the set |
| repository_sets.index | [GET /katello/api/repository_sets](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repository_sets/index.html)  | List repository sets. |
| repository_sets.show | [GET /katello/api/repository_sets/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repository_sets/show.html)  | Get info about a repository set |
| roles.clone | [POST /api/roles/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/roles/clone.html)  | Clone a role |
| roles.create | [POST /api/roles](https://theforeman.org/api/1.16/apidoc/v2/roles/create.html)  | Create a role |
| roles.destroy | [DELETE /api/roles/:id](https://theforeman.org/api/1.16/apidoc/v2/roles/destroy.html)  | Delete a role |
| roles.index | [GET /api/roles](https://theforeman.org/api/1.16/apidoc/v2/roles/index.html)  | List all roles |
| roles.show | [GET /api/roles/:id](https://theforeman.org/api/1.16/apidoc/v2/roles/show.html)  | Show a role |
| roles.update | [PUT /api/roles/:id](https://theforeman.org/api/1.16/apidoc/v2/roles/update.html)  | Update a role |
| roles.users_index | [GET /api/roles/:role_id/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users for role |
| scc_accounts.bulk_subscribe | [PUT /api/v2/scc_accounts/:id/bulk_subscribe](https://theforeman.org/api/1.16/apidoc/v2/scc_accounts/bulk_subscribe.html)  | Bulk subscription of scc_products for scc_account |
| scc_accounts.create | [POST /api/v2/scc_accounts](https://theforeman.org/api/1.16/apidoc/v2/scc_accounts/create.html)  | Create an scc_account |
| scc_accounts.destroy | [DELETE /api/v2/scc_accounts/:id](https://theforeman.org/api/1.16/apidoc/v2/scc_accounts/destroy.html)  | Delete scc_account |
| scc_accounts.index | [GET /api/v2/scc_accounts](https://theforeman.org/api/1.16/apidoc/v2/scc_accounts/index.html)  | List all scc_accounts |
| scc_accounts.scc_products_cc_showaccounts | [GET /api/v2/scc_accounts/:scc_account_id/scc_products/:id](https://theforeman.org/api/1.16/apidoc/v2/scc_products/show.html)  | Show an scc_account product |
| scc_accounts.scc_products_cc_subscribeaccounts | [PUT /api/v2/scc_accounts/:scc_account_id/scc_products/:id/subscribe](https://theforeman.org/api/1.16/apidoc/v2/scc_products/subscribe.html)  | Subscribe product |
| scc_accounts.scc_products_index | [GET /api/v2/scc_accounts/:scc_account_id/scc_products](https://theforeman.org/api/1.16/apidoc/v2/scc_products/index.html)  | List all products for scc_account |
| scc_accounts.show | [GET /api/v2/scc_accounts/:id](https://theforeman.org/api/1.16/apidoc/v2/scc_accounts/show.html)  | Show scc_account |
| scc_accounts.sync | [PUT /api/v2/scc_accounts/:id/sync](https://theforeman.org/api/1.16/apidoc/v2/scc_accounts/sync.html)  | Sync scc_account |
| scc_accounts.test_connection | [POST /api/v2/scc_accounts/test_connection](https://theforeman.org/api/1.16/apidoc/v2/scc_accounts/test_connection.html)  | Test connection for scc_account |
| scc_accounts.update | [PUT /api/v2/scc_accounts/:id](https://theforeman.org/api/1.16/apidoc/v2/scc_accounts/update.html)  | Update scc_account |
| settings.index | [GET /api/settings](https://theforeman.org/api/1.16/apidoc/v2/settings/index.html)  | List all settings |
| settings.show | [GET /api/settings/:id](https://theforeman.org/api/1.16/apidoc/v2/settings/show.html)  | Show a setting |
| settings.update | [PUT /api/settings/:id](https://theforeman.org/api/1.16/apidoc/v2/settings/update.html)  | Update a setting |
| smart_class_parameters.index | [GET /api/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List all smart class parameters |
| smart_class_parameters.override_values_create | [POST /api/smart_class_parameters/:smart_class_parameter_id/override_values](https://theforeman.org/api/1.16/apidoc/v2/override_values/create.html)  | Create an override value for a specific smart class parameter |
| smart_class_parameters.override_values_index | [GET /api/smart_class_parameters/:smart_class_parameter_id/override_values](https://theforeman.org/api/1.16/apidoc/v2/override_values/index.html)  | List of override values for a specific smart class parameter |
| smart_class_parameters.override_values_smart_class_parameter_id_override_destroyvalues | [DELETE /api/smart_class_parameters/:smart_class_parameter_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/destroy.html)  | Delete an override value for a specific smart class parameter |
| smart_class_parameters.override_values_smart_class_parameter_id_override_showvalues | [GET /api/smart_class_parameters/:smart_class_parameter_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/show.html)  | Show an override value for a specific smart class parameter |
| smart_class_parameters.override_values_smart_class_parameter_id_override_updatevalues | [PUT /api/smart_class_parameters/:smart_class_parameter_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/update.html)  | Update an override value for a specific smart class parameter |
| smart_class_parameters.show | [GET /api/smart_class_parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/show.html)  | Show a smart class parameter |
| smart_class_parameters.update | [PUT /api/smart_class_parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/update.html)  | Update a smart class parameter |
| smart_proxies.autosign_create | [POST /api/smart_proxies/:smart_proxy_id/autosign](https://theforeman.org/api/1.16/apidoc/v2/autosign/create.html)  | Create autosign entry |
| smart_proxies.autosign_index | [GET /api/smart_proxies/:smart_proxy_id/autosign](https://theforeman.org/api/1.16/apidoc/v2/autosign/index.html)  | List all autosign entries |
| smart_proxies.autosign_smart_proxy_id_destroyautosign | [DELETE /api/smart_proxies/:smart_proxy_id/autosign/:id](https://theforeman.org/api/1.16/apidoc/v2/autosign/destroy.html)  | Delete autosign entry |
| smart_proxies.create | [POST /api/smart_proxies](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/create.html)  | Create a smart proxy |
| smart_proxies.destroy | [DELETE /api/smart_proxies/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/destroy.html)  | Delete a smart proxy |
| smart_proxies.environments_import_puppetclasses | [POST /api/smart_proxies/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/environments/import_puppetclasses.html)  | Import puppet classes from puppet proxy |
| smart_proxies.environments_smart_proxy_id_import_puppetclassesenvironments | [POST /api/smart_proxies/:smart_proxy_id/environments/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/environments/import_puppetclasses.html)  | Import puppet classes from puppet proxy for an environment |
| smart_proxies.import_puppetclasses | [POST /api/smart_proxies/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/import_puppetclasses.html)  | Import puppet classes from puppet proxy |
| smart_proxies.index | [GET /api/smart_proxies](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/index.html)  | List all smart proxies |
| smart_proxies.refresh | [PUT /api/smart_proxies/:id/refresh](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/refresh.html)  | Refresh smart proxy features |
| smart_proxies.show | [GET /api/smart_proxies/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/show.html)  | Show a smart proxy |
| smart_proxies.smart_proxy_id_import_puppetclassesenvironments | [POST /api/smart_proxies/:smart_proxy_id/environments/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/import_puppetclasses.html)  | Import puppet classes from puppet proxy for an environment |
| smart_proxies.update | [PUT /api/smart_proxies/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/update.html)  | Update a smart proxy |
| smart_variables.create | [POST /api/smart_variables](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/create.html)  | Create a smart variable |
| smart_variables.destroy | [DELETE /api/smart_variables/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/destroy.html)  | Delete a smart variable |
| smart_variables.index | [GET /api/smart_variables](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/index.html)  | List all smart variables |
| smart_variables.override_values_create | [POST /api/smart_variables/:smart_variable_id/override_values](https://theforeman.org/api/1.16/apidoc/v2/override_values/create.html)  | Create an override value for a specific smart variable |
| smart_variables.override_values_index | [GET /api/smart_variables/:smart_variable_id/override_values](https://theforeman.org/api/1.16/apidoc/v2/override_values/index.html)  | List of override values for a specific smart variable |
| smart_variables.override_values_smart_variable_id_override_destroyvalues | [DELETE /api/smart_variables/:smart_variable_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/destroy.html)  | Delete an override value for a specific smart variable |
| smart_variables.override_values_smart_variable_id_override_showvalues | [GET /api/smart_variables/:smart_variable_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/show.html)  | Show an override value for a specific smart variable |
| smart_variables.override_values_smart_variable_id_override_updatevalues | [PUT /api/smart_variables/:smart_variable_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/update.html)  | Update an override value for a specific smart variable |
| smart_variables.show | [GET /api/smart_variables/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/show.html)  | Show a smart variable |
| smart_variables.update | [PUT /api/smart_variables/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/update.html)  | Update a smart variable |
| srpms.compare | [GET /katello/api/srpms/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/srpms/compare.html)  | List srpms |
| srpms.index | [GET /katello/api/srpms](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/srpms/index.html)  | List srpms |
| srpms.show | [GET /katello/api/srpms/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/srpms/show.html)  | Show SRPM details |
| statistics.index | [GET /api/statistics](https://theforeman.org/api/1.16/apidoc/v2/statistics/index.html)  | Get statistics |
| status.home_status | [GET /api/status](https://theforeman.org/api/1.16/apidoc/v2/home/status.html)  | Show status |
| status.ping_server_status | [GET /katello/api/status](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ping/server_status.html)  | Shows version information |
| statuses.ping_statuses | [GET /api/statuses](https://theforeman.org/api/1.16/apidoc/v2/ping/statuses.html)  | Shows status and version information of orcharhino system and it's subcomponents |
| subnets.create | [POST /api/subnets](https://theforeman.org/api/1.16/apidoc/v2/subnets/create.html)  | Create a subnet |
| subnets.destroy | [DELETE /api/subnets/:id](https://theforeman.org/api/1.16/apidoc/v2/subnets/destroy.html)  | Delete a subnet |
| subnets.domains_index | [GET /api/subnets/:subnet_id/domains](https://theforeman.org/api/1.16/apidoc/v2/domains/index.html)  | List of domains per subnet |
| subnets.freeip | [GET /api/subnets/:id/freeip](https://theforeman.org/api/1.16/apidoc/v2/subnets/freeip.html)  | Provides an unused IP address in this subnet |
| subnets.index | [GET /api/subnets](https://theforeman.org/api/1.16/apidoc/v2/subnets/index.html)  | List of subnets |
| subnets.interfaces_index | [GET /api/subnets/:subnet_id/interfaces](https://theforeman.org/api/1.16/apidoc/v2/interfaces/index.html)  | List all interfaces for subnet |
| subnets.parameters_create | [POST /api/subnets/:subnet_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for a subnet |
| subnets.parameters_index | [GET /api/subnets/:subnet_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for a subnet |
| subnets.parameters_reset | [DELETE /api/subnets/:subnet_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameters for a subnet |
| subnets.parameters_subnet_id_destroyparameters | [DELETE /api/subnets/:subnet_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for a subnet |
| subnets.parameters_subnet_id_showparameters | [GET /api/subnets/:subnet_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for a subnet |
| subnets.parameters_subnet_id_updateparameters | [PUT /api/subnets/:subnet_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for a subnet |
| subnets.show | [GET /api/subnets/:id](https://theforeman.org/api/1.16/apidoc/v2/subnets/show.html)  | Show a subnet |
| subnets.update | [PUT /api/subnets/:id](https://theforeman.org/api/1.16/apidoc/v2/subnets/update.html)  | Update a subnet |
| subscriptions.index | [GET /katello/api/subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/index.html)  |  |
| subscriptions.products_index | [GET /katello/api/subscriptions/:subscription_id/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List of subscription products in a subscription |
| subscriptions.show | [GET /katello/api/subscriptions/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/show.html)  | Show a subscription |
| sync_plans.destroy | [DELETE /katello/api/sync_plans/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/destroy.html)  | Destroy a sync plan |
| sync_plans.index | [GET /katello/api/sync_plans](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/index.html)  | List sync plans |
| sync_plans.products_index | [GET /katello/api/sync_plans/:sync_plan_id/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List of Products for sync plan |
| sync_plans.show | [GET /katello/api/sync_plans/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/show.html)  | Show a sync plan |
| sync_plans.sync | [PUT /katello/api/sync_plans/:id/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/sync.html)  | Initiate a sync of the products attached to the sync plan |
| sync_plans.update | [PUT /katello/api/sync_plans/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/update.html)  | Update a sync plan |
| template_combinations.destroy | [DELETE /api/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/destroy.html)  | Delete a template combination |
| template_combinations.show | [GET /api/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/show.html)  | Show template combination |
| template_kinds.index | [GET /api/template_kinds](https://theforeman.org/api/1.16/apidoc/v2/template_kinds/index.html)  | List all template kinds |
| templates.foreign_input_sets_create | [POST /api/templates/:template_id/foreign_input_sets](https://theforeman.org/api/1.16/apidoc/v2/foreign_input_sets/create.html)  | Create a foreign input set |
| templates.foreign_input_sets_index | [GET /api/templates/:template_id/foreign_input_sets](https://theforeman.org/api/1.16/apidoc/v2/foreign_input_sets/index.html)  | List foreign input sets |
| templates.foreign_input_sets_template_id_foreign_input_destroysets | [DELETE /api/templates/:template_id/foreign_input_sets/:id](https://theforeman.org/api/1.16/apidoc/v2/foreign_input_sets/destroy.html)  | Delete a foreign input set |
| templates.foreign_input_sets_template_id_foreign_input_showsets | [GET /api/templates/:template_id/foreign_input_sets/:id](https://theforeman.org/api/1.16/apidoc/v2/foreign_input_sets/show.html)  | Show foreign input set details |
| templates.foreign_input_sets_template_id_foreign_input_updatesets | [PUT /api/templates/:template_id/foreign_input_sets/:id](https://theforeman.org/api/1.16/apidoc/v2/foreign_input_sets/update.html)  | Update a foreign input set |
| templates.template_export | [POST /api/templates/export](https://theforeman.org/api/1.16/apidoc/v2/template/export.html)  | Initiate Export |
| templates.template_import_ | [POST /api/templates/import](https://theforeman.org/api/1.16/apidoc/v2/template/import.html)  | Initiate Import |
| templates.template_inputs_create | [POST /api/templates/:template_id/template_inputs](https://theforeman.org/api/1.16/apidoc/v2/template_inputs/create.html)  | Create a template input |
| templates.template_inputs_index | [GET /api/templates/:template_id/template_inputs](https://theforeman.org/api/1.16/apidoc/v2/template_inputs/index.html)  | List template inputs |
| templates.template_inputs_template_id_template_destroyinputs | [DELETE /api/templates/:template_id/template_inputs/:id](https://theforeman.org/api/1.16/apidoc/v2/template_inputs/destroy.html)  | Delete a template input |
| templates.template_inputs_template_id_template_showinputs | [GET /api/templates/:template_id/template_inputs/:id](https://theforeman.org/api/1.16/apidoc/v2/template_inputs/show.html)  | Show template input details |
| templates.template_inputs_template_id_template_updateinputs | [PUT /api/templates/:template_id/template_inputs/:id](https://theforeman.org/api/1.16/apidoc/v2/template_inputs/update.html)  | Update a template input |
| trends.create | [POST /api/trends](https://theforeman.org/api/1.16/apidoc/v2/trends/create.html)  | Create a trend counter |
| trends.destroy | [DELETE /api/trends/:id](https://theforeman.org/api/1.16/apidoc/v2/trends/destroy.html)  | Delete a trend counter |
| trends.index | [GET /api/trends](https://theforeman.org/api/1.16/apidoc/v2/trends/index.html)  | List of trends counters |
| trends.show | [GET /api/trends/:id](https://theforeman.org/api/1.16/apidoc/v2/trends/show.html)  | Show a trend |
| usergroups.create | [POST /api/usergroups](https://theforeman.org/api/1.16/apidoc/v2/usergroups/create.html)  | Create a user group |
| usergroups.destroy | [DELETE /api/usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/usergroups/destroy.html)  | Delete a user group |
| usergroups.external_usergroups_create | [POST /api/usergroups/:usergroup_id/external_usergroups](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/create.html)  | Create an external user group linked to a user group |
| usergroups.external_usergroups_index | [GET /api/usergroups/:usergroup_id/external_usergroups](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/index.html)  | List all external user groups for user group |
| usergroups.external_usergroups_usergroup_id_external_destroyusergroups | [DELETE /api/usergroups/:usergroup_id/external_usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/destroy.html)  | Delete an external user group |
| usergroups.external_usergroups_usergroup_id_external_refreshusergroups | [PUT /api/usergroups/:usergroup_id/external_usergroups/:id/refresh](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/refresh.html)  | Refresh external user group |
| usergroups.external_usergroups_usergroup_id_external_showusergroups | [GET /api/usergroups/:usergroup_id/external_usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/show.html)  | Show an external user group for user group |
| usergroups.external_usergroups_usergroup_id_external_updateusergroups | [PUT /api/usergroups/:usergroup_id/external_usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/update.html)  | Update external user group |
| usergroups.index | [GET /api/usergroups](https://theforeman.org/api/1.16/apidoc/v2/usergroups/index.html)  | List all user groups |
| usergroups.show | [GET /api/usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/usergroups/show.html)  | Show a user group |
| usergroups.update | [PUT /api/usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/usergroups/update.html)  | Update a user group |
| usergroups.users_index | [GET /api/usergroups/:usergroup_id/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users for user group |
| users.create | [POST /api/users](https://theforeman.org/api/1.16/apidoc/v2/users/create.html)  | Create a user |
| users.destroy | [DELETE /api/users/:id](https://theforeman.org/api/1.16/apidoc/v2/users/destroy.html)  | Delete a user |
| users.index | [GET /api/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users |
| users.personal_access_tokens_create | [POST /api/users/:user_id/personal_access_tokens](https://theforeman.org/api/1.16/apidoc/v2/personal_access_tokens/create.html)  | Create a Personal Access Token for a user |
| users.personal_access_tokens_index | [GET /api/users/:user_id/personal_access_tokens](https://theforeman.org/api/1.16/apidoc/v2/personal_access_tokens/index.html)  | List all Personal Access Tokens for a user |
| users.personal_access_tokens_user_id_personal_access_destroytokens | [DELETE /api/users/:user_id/personal_access_tokens/:id](https://theforeman.org/api/1.16/apidoc/v2/personal_access_tokens/destroy.html)  | Revoke a Personal Access Token for a user |
| users.personal_access_tokens_user_id_personal_access_showtokens | [GET /api/users/:user_id/personal_access_tokens/:id](https://theforeman.org/api/1.16/apidoc/v2/personal_access_tokens/show.html)  | Show a Personal Access Token for a user |
| users.show | [GET /api/users/:id](https://theforeman.org/api/1.16/apidoc/v2/users/show.html)  | Show a user |
| users.ssh_keys_create | [POST /api/users/:user_id/ssh_keys](https://theforeman.org/api/1.16/apidoc/v2/ssh_keys/create.html)  | Add an SSH key for a user |
| users.ssh_keys_index | [GET /api/users/:user_id/ssh_keys](https://theforeman.org/api/1.16/apidoc/v2/ssh_keys/index.html)  | List all SSH keys for a user |
| users.ssh_keys_user_id_ssh_destroykeys | [DELETE /api/users/:user_id/ssh_keys/:id](https://theforeman.org/api/1.16/apidoc/v2/ssh_keys/destroy.html)  | Delete an SSH key for a user |
| users.ssh_keys_user_id_ssh_showkeys | [GET /api/users/:user_id/ssh_keys/:id](https://theforeman.org/api/1.16/apidoc/v2/ssh_keys/show.html)  | Show an SSH key from a user |
| users.table_preferences_create | [POST /api/users/:user_id/table_preferences](https://theforeman.org/api/1.16/apidoc/v2/table_preferences/create.html)  | Creates a table preference for a given table |
| users.table_preferences_index | [GET /api/users/:user_id/table_preferences](https://theforeman.org/api/1.16/apidoc/v2/table_preferences/index.html)  | List of table preferences for a user |
| users.table_preferences_user_id_table_destroypreferences | [DELETE /api/users/:user_id/table_preferences/:name](https://theforeman.org/api/1.16/apidoc/v2/table_preferences/destroy.html)  | Delete a table preference for a given table |
| users.table_preferences_user_id_table_showpreferences | [GET /api/users/:user_id/table_preferences/:name](https://theforeman.org/api/1.16/apidoc/v2/table_preferences/show.html)  | Table preference details of a given table |
| users.table_preferences_user_id_table_updatepreferences | [PUT /api/users/:user_id/table_preferences/:name](https://theforeman.org/api/1.16/apidoc/v2/table_preferences/update.html)  | Updates a table preference for a given table |
| users.update | [PUT /api/users/:id](https://theforeman.org/api/1.16/apidoc/v2/users/update.html)  | Update a user |
