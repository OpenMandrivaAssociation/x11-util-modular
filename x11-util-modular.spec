Name: x11-util-modular
BuildArch: noarch
Summary: Set of scripts to manage modular X.org packages
Version: 0.0.1
Release: %mkrel 1
Group: Development/X11
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/util/modular xorg/util/modular
# cd xorg/util/modular
# git-archive --format=tar --prefix=x11-util-modular-0.0.1/ xorg-modular-0.0.1@mandriva | bzip2 -9 > x11-util-modular-0.0.1.tar.bz2
########################################################################
Source0: %{name}-%{version}.tar.bz2
License: GPLv2+ and MIT
########################################################################
# git format-patch xorg-modular-0.0.1@mandriva..mandriva+gpl
Patch1: 0001-Initial-set-of-scripts-to-check-for-package-dependen.patch
########################################################################

%description
Scripts used for X.org package management.

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1

%build

%install
#rm -rf %{buildroot}
for script in \
	x-build.pl \
	x-check-deps.pl \
	x-check-rpm-deps.pl \
	x-check-symbols.pl \
	; do
	install -D -m 755 mandriva/bin/$script %{buildroot}/%{_bindir}/$script
done

for doc in \
	git.txt \
	README.building \
	x-check-symbols.pl.txt \
	README \
	x-check-deps.pl.txt \
	; do
	install -D -m 644 mandriva/docs/$doc %{buildroot}/%{_docdir}/%{name}/$doc
done

# Directory to store dependency files
mkdir -p %{buildroot}/%{_datadir}/X11/mandriva

%clean
#rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*.pl
%doc %{_docdir}/%{name}/*
%dir %{_datadir}/X11/mandriva
