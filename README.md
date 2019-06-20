# build_tools
Assorted build tools for building software. 

## CLI-front end to mako

[Mako Templates](https://www.makotemplates.org/) provide a clean way to add
extended functionality to plain-text file processing. Commonly used to 
dynamically create HTML, they can also be used during a build process to
add templating features to things like Dockerfiles. 

Generic makefile rule for templating Dockerfiles:

```
%/Dockerfile.gen: %/Dockerfile.mako
	echo $@ $<
	./build_tools/makocc.py -o $@ $<
```

Example dockerfile (uses included multiArch module)

```
<%!
  import multiArch
%>
FROM ubuntu:latest as MyDockerImage
% if multiArch.arch!=multiArch.host:
#copy over qemu for "cross-compiled" builds
COPY containers/qemu_support/qemu-aarch64-static /usr/bin

## Do things if we are cross building

% endif
```

## Version generation

`version.sh` is a shell script to generate a verison.py containing generic
build information (git branch, time, etc.) 

It takes an argument to the directory of the repo to version (default=pwd)



