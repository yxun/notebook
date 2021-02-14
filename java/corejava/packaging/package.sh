#!/bin/bash

# make a new JAR file
jar cvf [JAR filename.jar] File1 File2 ...

# m adds a manifest to the JAR file
# t displays the table of contents
# u updates an existing JAR file
# x extracts files

# manifest file MANIFEST.MF IN META-INF subdirectory, the last line in the manifest must end with a newline
# create a new JAR with a manifest
jar cfm MyArchive.jar manifest.mf *.class

# update the manifest of an existing JAR file
jar ufm MyArchive.jar manifest-additions.mf

# specify the entry point 
jar cvfe MyProgram.jar [MainAppClass] [files to add]
# Alternatively in the manifest
# Main-Class: MainAppClass

# start the program
java -jar MyProgram.jar

# sealing a package, then no class outside the sealed archive can be defined
# Sealed: true   into the main section of the manifest

# Properties, useful in specifying configuration options

# freely accessible system properties in the file security/java.policy in the directory of the Java runtime

# Preferences

