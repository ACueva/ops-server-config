import arcpy
import sys
import os


def usage():
    print("creategdbs.py <Source Folder> <Destination Folder>")


def getfolders(path, patterns):
    matching_file_list = [os.path.join(dp, f) for dp, dn, filenames in \
                          os.walk(path) for f in filenames if os.path.splitext(f)[1] in patterns]
    return matching_file_list

if len(sys.argv) < 3:
    usage()
    sys.exit(-1)

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

print("Source Folder is " + source_folder)
print("Creating databases in " + destination_folder)

destination_dblist =[]

source_dblist = getfolders(source_folder, [".sde"])
print("Source databases found: " + str(source_dblist))

print("Stripping extension and path from source database list")
for sourcedb in source_dblist:
    filename = os.path.split(sourcedb)[1]
    filename_noext = os.path.splitext(filename)[0]
    print(filename_noext)
    destination_dblist.append(filename_noext)

print("Destination databases to create: " + str(destination_dblist))

for database in destination_dblist:
    try:

        tempdb = database + ".gdb"
        print("Creating " + tempdb)
        arcpy.CreateFileGDB_management(destination_folder, tempdb)

    except arcpy.ExecuteError as arcpy_error:
        pass