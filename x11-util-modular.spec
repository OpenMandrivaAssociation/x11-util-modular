Name: x11-util-modular
BuildArch: noarch
Summary: Set of scripts to manage modular X.org packages
Version: 0.5
Release: %mkrel 1
Group: Development/X11
########################################################################
# git clone git://anongit.freedesktop.org/xorg/util/modular xorg/util/modular
# cd xorg/util/modular
# git-archive --format=tar --prefix=%{name}-%{version}/ d58fd2e3668c8940d5d0ebe4b9b3057eee7aa5ce | bzip2 -9 > %{name}-%{version}.tar.bz2
########################################################################
Source0: %{name}-%{version}.tar.bz2
License: GPLv2+ and MIT

Requires: perl sudo
Requires: git-core cvs
Requires: make gcc bison flex autoconf
Requires: glibc-devel freetype2-devel
Requires: strace wget

Patch1: 0001-Add-a-set-of-scripts-to-allow-easier-build-of-xorg-l.patch

%description
Scripts used for X.org package management.

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1

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
