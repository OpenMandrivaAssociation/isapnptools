Summary:	Utilities for configuring ISA Plug-and-Play (PnP) devices
Name:		isapnptools
Version:	1.26
Release:	%mkrel 13
License:	GPL
Group:		System/Configuration/Hardware
URL:		ftp://ftp.demon.co.uk/pub/unix/linux/utils/
Source0:	%{name}-%{version}.tar.bz2
Patch1:		%{name}-demo2.patch
Patch2:		isapnptools-1.26-gcc4-fix.patch
Patch3:		isapnptools-1.26-format_not_a_string_literal_and_no_format_arguments.diff
ExclusiveArch:	%{ix86} alpha
BuildRequires:	flex
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

Install isapnptools-devel if you need to do development with ISA PnP
cards.

%prep

%setup -q
%patch1 -p1
%patch2 -p1 -b .gcc4
%patch3 -p0 -b .format_not_a_string_literal_and_no_format_arguments

find | xargs chmod u+w

%build
%configure --sbindir=/sbin
make RPM_OPT_FLAGS="%{optflags}"
perl -pi -e "s/^\([^#]\)/#\1/" etc/isapnp.gone
%ifarch alpha
perl -pi -e "s/#IRQ 7/IRQ 7/" etc/isapnp.gone
%endif 

%install
rm -rf %{buildroot}

%makeinstall_std
install -m644 etc/isapnp.gone -D %{buildroot}%{_sysconfdir}/isapnp.gone

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,755)
%doc README
%doc config-scripts/YMH0021
%config(missingok,noreplace) %attr(0644,root,root) %{_sysconfdir}/isapnp.gone
/sbin/*
%{_mandir}/man*/*

%files devel
%defattr(-,root,root,755)
%doc AUTHORS COPYING NEWS doc
%{_libdir}/*.a
%{_includedir}/isapnp


