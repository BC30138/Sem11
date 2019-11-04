# LAB 1

go-xcat install

Возможно придется записать в .bashrc содержимое файла /etc/profile.d/xcat.sh

```sh
$ vim /etc/hostnames  
```
Изменить имя-хоста на имя-хоста.домен.

У меня был bc30138vm -> bc30138vm.cluster

```sh
$ vim /etc/hosts
```

Изменить вторую строку на 

<свой ip (10.0.2.160)> bc30138.cluster mgmt

```sh
$ vim /etc/resolvconf/resolv.conf.d/base
```

Сюда записать 
```
search cluster
```

Примонтировать диск с образом iso системы. 

Создадим образы xcat: 

```
$ copycds-cdrom
```

Проверить работу команды можно следующим образом:

```
$ tabdump osimage
```

Список должен содержать как минимум три образа.

Далее надо настроить dns, мне пришлось выполнить следующие команды:
```
$ chdef -t site domain="cluster"
$ makedns -n
```

Далее надо настроить dhcp:
```
$ chdef -t site dhcpinterfaces="enp0s3"
$ makedhcp -n
```
