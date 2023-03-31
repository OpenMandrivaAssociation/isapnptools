Summary:	Utilities for configuring ISA Plug-and-Play (PnP) devices
Name:		isapnptools
Version:	1.27
Release:	12
License:	GPLv2
Group:		System/Configuration/Hardware
Url:		http://www.roestock.demon.co.uk/isapnptools/
Source0:	ftp://metalab.unc.edu/pub/Linux/system/hardware/%{name}-%{version}.tgz
Patch1:		%{name}-demo2.patch
Patch2:		isapnptools-1.27-include.patch
Patch3:		isapnptools-1.26-format_not_a_string_literal_and_no_format_arguments.diff

BuildRequires:	flex

%description
The isapnptools package contains utilities for configuring ISA
Plug-and-Play (PnP) cards which are in compliance with the PnP ISA
Specification Version 1.0a.  ISA PnP cards use registers instead of
jumpers for setting the board address and interrupt assignments.  The
cards also contain descriptions of the resources which need to be
allocated.  The BIOS on your system, or isapnptools, uses a protocol
described in the specification to find all of the PnP boards and
allocate the resources so that none of them conflict.

Note that the BIOS doesn't do a very good job of allocating resources.
So isapnptools is suitable for all systems, whether or not they
include a PnP BIOS. In fact, a PnP BIOS adds some complications.  A
PnP BIOS may already activate some cards so that the drivers can find
them.  Then these tools can unconfigure them or change their settings,
causing all sorts of nasty effects. If you have PnP network cards that
already work, you should read through the documentation files very
carefully before you use isapnptools.

Install isapnptools if you need utilities for configuring ISA PnP
cards.

%package	devel
Summary:	Devel libraries for configuring ISA Plug-and-Play (PnP) devices
Group:		Development/C

%description	devel
Install isapnptools-devel if you need to do development with ISA PnP
cards.

%prep

%setup -q
%autopatch -p1

find | xargs chmod u+w

%build
%configure2_5x --sbindir=/sbin
make RPM_OPT_FLAGS="%{optflags}"
sed -i -e "s/^\([^#]\)/#\1/" etc/isapnp.gone
%ifarch alpha
sed -i -e "s/#IRQ 7/IRQ 7/" etc/isapnp.gone
%endif 

%install
%makeinstall_std
install -m644 etc/isapnp.gone -D %{buildroot}%{_sysconfdir}/isapnp.gone

%files
%doc README
%doc config-scripts/YMH0021
%config(missingok,noreplace) %attr(0644,root,root) %{_sysconfdir}/isapnp.gone
/sbin/*
%{_mandir}/man*/*

%files devel
%doc AUTHORS COPYING NEWS doc
%{_libdir}/*.a
%{_includedir}/isapnp

