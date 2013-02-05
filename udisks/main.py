#!/usr/bin/python
# coding: utf-8
# Copyright (C) 2011 Lucas Alvares Gomes <lucasagomes@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import udisks


def main():
    ud = udisks.UDisks()
    print("EnumerateAdapters")
    for adp in ud.EnumerateAdapters():
        print(adp.NativePath)
    print("EnumerateExpanders")
    for adp in ud.EnumerateExpanders():
        print(adp.NativePath)
    print("EnumeratePorts")
    for adp in ud.EnumeratePorts():
        print(adp.NativePath)

    # print("EnumerateDeviceFiles")
    # for dev in ud.EnumerateDeviceFiles():
    # 	print(dev)
    print("EnumerateDevices")
    for dev in ud.EnumerateDevices():
        # print(dev.NativePath)
        # print(dev.DriveModel, dev.DriveRotationRate)
        # print(dev.DeviceFile, dev.IdLabel, dev.PartitionType, dev.PartitionUuid, dev.DeviceIsRemovable, dev.DeviceIsPartition, dev.DeviceIsMounted)
        # print(dev.DeviceFile)
        print(dev.GetInfoDevice())
        if dev.DeviceIsPartition:
            print(dev.GetInfoPartition())


if __name__ == '__main__':
    main()
