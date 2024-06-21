[![build-test](https://github.com/darkwizard242/ansible-role-goofys/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-goofys/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-goofys/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-goofys/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/goofys) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-goofys&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-goofys) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-goofys&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-goofys) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-goofys&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-goofys) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-goofys?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-goofys?color=orange&style=flat-square)

# Ansible Role: goofys

Role to install (_by default_) `goofys` on **Debian/Ubuntu** and **EL** systems. [goofys](https://github.com/kahing/goofys) is a high-performance, POSIX-ish Amazon S3 file system written in Go.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
goofys_app: goofys
goofys_version: 0.24.0
goofys_dl_url: https://github.com/kahing/{{ goofys_app }}/releases/download/v{{ goofys_version }}/{{ goofys_app }}
goofys_bin_path: /usr/local/bin
goofys_file_owner: root
goofys_file_group: root
goofys_file_mode: '0755'
```

### Variables table:

Variable         | Description
---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------
goofys_app       | Defines the app to install i.e. **goofys**
goofys_version   | Defined to dynamically fetch the desired version to install. Defaults to: **0.24.0**
goofys_dl_url    | Defines URL to download the goofys binary from.
goofys_bin_path  | Defined to dynamically set the appropriate path to store goofys binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
goofys_owner     | Owner for the binary file of goofys.
goofys_group     | Group for the binary file of goofys.
goofys_file_mode | Mode for the binary file of goofys.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **goofys**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.goofys
```

For customizing behavior of role (i.e. specifying the desired **goofys** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.goofys
  vars:
    goofys_version: 0.23.1
```

For customizing behavior of role (i.e. placing binary of **goofys** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.goofys
  vars:
    goofys_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-goofys/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
