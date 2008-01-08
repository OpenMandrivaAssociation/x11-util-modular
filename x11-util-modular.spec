Name: x11-util-modular
BuildArch: noarch
Summary: Set of scripts to manage modular X.org packages
Version: 0.0.1
Release: %mkrel 4
Group: Development/X11
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/util/modular xorg/util/modular
# cd xorg/util/modular
# git-archive --format=tar --prefix=x11-util-modular-0.0.1/ xorg-modular-0.0.1@mandriva | bzip2 -9 > x11-util-modular-0.0.1.tar.bz2
########################################################################
Source0: %{name}-%{version}.tar.bz2
# Fixme - implement a better method to make available this information
Source1: depsdir.tar.bz2
License: GPLv2+ and MIT
########################################################################
# git format-patch xorg-modular-0.0.1@mandriva..mandriva+gpl
Patch1: 0001-Initial-set-of-scripts-to-check-for-package-dependen.patch
Patch2: 0002-Fix-some-typos-and-reflect-correction-of-repository.patch
Patch3: 0003-Initial-support-to-also-allow-building-from-tarballs.patch
Patch4: 0004-Add-several-new-options-to-x-build.pl-including-c.patch
Patch5: 0005-Fix-hash-reference-in-update-properly-handle-mod.patch
Patch6: 0006-Bug-fixes-including-better-help-for-setting-defaul.patch
Patch7: 0007-Add-complete-support-for-generating-the-data-files.patch
Patch8: 0008-Changed-to-require-installing-rpms-as-they-are-bui.patch
Patch9: 0009-Add-more-packages-and-better-error-check-to-x-buil.patch
########################################################################

%description
Scripts used for X.org package management.

%prep
%setup -q -c %{name}-%{version} -b1

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build

%install
rm -rf %{buildroot}
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
for file in depsdir/*.deps depsdir/*.list; do
    install -m 644 $file %{buildroot}/%{_datadir}/X11/mandriva
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*.pl
%doc %{_docdir}/%{name}/*
%dir %{_datadir}/X11/mandriva
%{_datadir}/X11/mandriva/*
