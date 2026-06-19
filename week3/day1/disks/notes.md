# Practical skills for day 1

## dd - Backuping disks and creating disk images

### Create a 2GB disk image
`dd if=/dev/zero of=/path/to/image.img bs=1G count=2`

### Backup a whole disk
`dd if=/dev/sdb of=/dev/sdc`

## losetup - Make a loop device to act as a block disk
`losetup --find --show /path/to/image.img`

## gdisk - Making GPT partitions
- `gdisk`
- `n # Create a new partition`
- `1 # Give the partition a num`
- `<somenum> # Give the partition firts sector `
- `<somenum> # Give the partition Last sector`
- `L # Show all cods to give the partition a type` 
- `<hex-code> # Give the partition a type`
- `w # Write all the changes` or `q # Quit from all the changes`


## Physical volume
### List all physical volume
`pvdisplay`

### Create a physical volume
`pvcreate /dev/path/to/block/device`

### Resize a physical volume
When the partition got more space (by gdisk for example) <br/>
`pvresize /dev/path/to/block/device # To update up to the partiton's extended space` 

When you need to shrink the partition space <br/>
`pvresize --setphysicalvolumesize <size> /dev/path/to/block/device` 

### Delete a physical volume
`pvcremove /dev/path/to/block/device`

## Volume group
### List all volume groups
`vgdisplay`

### Create a volume group
`vgcreate <vg-name> /dev/path/to/block/device # which was added as a physical volume (could be plural physical volumes)`

### Resize a volume group
`vgextend <vg-name> /dev/path/to/additional/block/device` 

### Remove a volume group
`vgremove <vg-name>`

### Exclude a physical volume from a volume group
`vgreduce <vg-name> /dev/path/to/block/device`

## Logical volume
### List all logical volumes
`lsdisplay`

### Create a logical volume
With actual size (50G, 400G etc)
`lvcreate -L <size> --name <lv-name> <vg-name>`
With free precents of a volume group
`lvcreate -l <number>%FREE --name <lv-name> <vg-name>`

### Resize a logical volume
With an actual size (50G, 400G etc)
`lvresize -L <size> --name <lv-name> <vg-name>`
With extending an actual size (+50G, +100G etc)
`lvresize -L +<size> --name <lv-name> <vg-name>`
With shrinking an actual size (-50G, -70G etc)
`lvreduce --resizefs -L -<size> --name <lv-name> <vg-name>`

With free precents of a volume group
`lvresize -l <number>%FREE --name <lv-name> <vg-name>`
With extending free precents of a volume group 
`lvresize -L +<number>%FREE --name <lv-name> <vg-name>`

### Remove a logical volume
`lsremove <lv-name>`

### How path to a logical volume looks like
`/dev/<vg-name>/<lv-name>`

## Mount, umount
### Mount a block device (bd), logical volume (lv)
`mount /dev/path/to/device /path/to/dir`

### Unmount a bd/lv
`mount /dev/path/to/device`

### Add auto mounting with booting up the system
- Add a bd/lv to /etc/fstab
```bash
# /etc/fstab
/dev/mapper/debian--vg-root /               ext4    errors=remount-ro 0       1

#/dev/mapper/debian--vg-root - Or UUID of the device/lv
# / - /path/to/dir
# ext4 - file system name
# defaults - options
# 0 - 0
# 1 - is the device mandatory in bool
```
- `systmectl daemon-reload`
- `mount -a # To check for mistates`

## File system
### Build an ext4 file system
`mkfs.ext4 /dev/path/to/device`

### Resize an ext4 fs after updating a device size
`resize2fs dev/path/to/device`