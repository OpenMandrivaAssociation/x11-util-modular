Name: x11-util-modular
BuildArch: noarch
Summary: Set of scripts to manage modular X.org packages
Version: 0.0.2
Release: %mkrel 2
Group: Development/X11
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/util/modular xorg/util/modular
# cd xorg/util/modular
# git-archive --format=tar --prefix=x11-util-modular-0.0.2/ xorg-modular-0.0.2@mandriva | bzip2 -9 > x11-util-modular-0.0.2.tar.bz2
########################################################################
Source0: %{name}-%{version}.tar.bz2
# Fixme - implement a better method to make available this information
Source1: depsdir.tar.bz2
License: GPLv2+ and MIT
########################################################################
# git format-patch xorg-modular-0.0.2@mandriva..mandriva+gpl
########################################################################

%description
Scripts used for X.org package management.

%prep
%setup -q -a1

%build

%install
rm -rf %{buildroot}

# Directory to store dependency files
mkdir -p %{buildroot}/%{_datadir}/X11/mandriva
for file in depsdir/*.deps depsdir/*.list; do
    install -m 644 $file %{buildroot}/%{_datadir}/X11/mandriva
done

for script in \
	x-build.pl \
	x-trace.pl \
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*.pl
%doc %{_docdir}/%{name}/*
%dir %{_datadir}/X11/mandriva
%{_datadir}/X11/mandriva/*
