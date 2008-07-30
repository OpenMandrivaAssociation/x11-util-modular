Name: x11-util-modular
BuildArch: noarch
Summary: Set of scripts to manage modular X.org packages
Version: 0.0.2
Release: %mkrel 9
Group: Development/X11
########################################################################
# git clone git://anongit.freedesktop.org/xorg/util/modular xorg/util/modular
# cd xorg/util/modular
# git-archive --format=tar --prefix=x11-util-modular-0.0.2/ a78aabbfdadafcc6fa802f6bf45c832e645bc191 | bzip2 -9 > x11-util-modular-0.0.2.tar.bz2
########################################################################
Source0: %{name}-%{version}.tar.bz2
License: GPLv2+ and MIT
BuildRoot: %{_tmppath}/%{name}-root

Requires: perl sudo
Requires: git-core cvs
Requires: make gcc bison flex autoconf
Requires: glibc-devel freetype2-devel
Requires: strace wget

# git-format-patch master..patches
Patch1: 0001-Add-a-set-of-scripts-to-allow-easier-build-of-xorg-l.patch
Patch2: 0002-Update-to-latest-version-of-build-scripts.patch
Patch3: 0003-Update-to-latest-build-scripts.patch
Patch4: 0004-Update-for-rpm-build-and-current-git-master.patch
Patch5: 0005-Update-rpm-build-to-match-Mandriva-cooker.patch
Patch6: 0006-Update-script-to-build-a-xorg-snapshot-and-the-rpm-b.patch
Patch7: 0007-Update-build-scripts-to-match-latest-build-requirem.patch
Patch8: 0008-Update-to-latest-build-of-snapshot-packages.patch

%description
Scripts used for X.org package management.

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build

%install
rm -rf %{buildroot}

pushd xorg-scripts
for script in *.pl; do
	install -D -m 755 $script %{buildroot}/%{_bindir}/$script
done
install -D -m 644 xorg-scripts.txt %{buildroot}/%{_docdir}/%{name}/xorg-scripts.txt
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*.pl
%doc %{_docdir}/%{name}/*
