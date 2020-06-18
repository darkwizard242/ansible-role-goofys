[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-goofys.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-goofys) ![Ansible Role](https://img.shields.io/ansible/role/48533?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/48533?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/48533?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-goofys&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-goofys) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-goofys?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-goofys?color=orange&style=flat-square)

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
goofys_bin_path: "/usr/local/bin/{{ goofys_app }}"
goofys_bin_permission_mode: '0755'
```

### Variables table:

Variable                   | Value (default)                                                                                       | Description
-------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------
goofys_app                 | goofys                                                                                                | Defines the app to install i.e. **goofys**
goofys_version             | 0.24.0                                                                                                | Defined to dynamically fetch the desired version to install. Defaults to: **0.24.0**
goofys_dl_url              | <https://github.com/kahing/{{> goofys_app }}/releases/download/v{{ goofys_version }}/{{ goofys_app }} | Defines URL to download the goofys binary from.
goofys_bin_path            | "/usr/local/bin/{{ goofys_app }}"                                                                     | Defined to dynamically set the appropriate path to store goofys binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin/goofys**
goofys_bin_permission_mode | '0755'                                                                                                | Defines the permission mode level for the file.

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
