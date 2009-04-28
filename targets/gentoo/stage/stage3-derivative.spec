# This file defines common settings for all stage3 derivatives.  Stage3
# derivatives are those targets that are generated directly from a stage3, and
# include stage3-freshen, stage3-quick, stage4, openvz and vserver. A target
# can be both a stage3 generator and a stage3 derivative -- stage3-freshen and
# stage3-quick are two examples.

[section path/mirror]

source: $[:source/subpath]/$[source/name].tar.bz2

[section source]

: stage3
name: $[]-$[:subarch]-$[:version]

# When building from a stage3, use the last sucessfully built stage3:

version: << $[path/mirror/control]/lastdate
subarch: << $[path/mirror/control]/subarch
build: << $[path/mirror/control]/build


