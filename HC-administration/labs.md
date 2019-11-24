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
```

Установить диапазон адресов для dhcp.

```
$ chdef -t network 10_0_2_0-255_255_255_0 dynamicrange="10.0.2.51-10.0.2.80"
$ makedhcp -n
$ makedhcp -a
```

Создать пользователя root на каждой машине c паролем abc123
```
$ chtab key=system passwd.username=root passwd.password=`openssl passwd -1 abc123`
```

Создаем calculation ноды - создаем новую виртуальную машину Linux (Ubuntu 64) с памятью 1280мб и жестким диском 20Гб
Настройка виртуальной машины для нода: 
- Вкладка System: 
  - Motherboard/Boot order отключить Floppy и Optical, включить Network, пододвинуть наверх в последовательности 1 - Hard, 2 - Network.
  - Motherboard/Chipset = ICH9
  - Motherboard/Pointing Device = PS/2 Mouse
  - Motherboard/Extended Features = снять галку Hardware Clock
  - Processor/Processor(s) = 2
  - Processor/Execution Cap = 60
  - Processor/Extended Features = поставить галку Enable PAE
- Storage:
  - Удалить Controller: IDE
- Audio
  - Убрать галку Enable audio 
- Network:
  - Attached to: NAT Network
  - Name: NatNetwork
  - Запомнить макадрес, у меня 080027C8D369

Создаем узел calcnode:
```
$ mkdef -t node -o calcnode01 arch=x86_64 mac="08:00:27:C8:D3:69" ip="10.0.2.101" netboot="pxe" groups="all"
$ makehosts calcnode01
```

Связываем нод с образом системы
```
$ nodeset calcnode01 osimage=ubuntu16.04.6-x86_64-install-compute
```

запускаем виртуальный нод?