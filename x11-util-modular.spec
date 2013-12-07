Name:		x11-util-modular
Summary:	Set of scripts to manage modular X.org packages
Version:	0.0.2
Release:	18
Group:		Development/X11
########################################################################
# git clone git://anongit.freedesktop.org/xorg/util/modular xorg/util/modular
# cd xorg/util/modular
# git-archive --format=tar --prefix=x11-util-modular-0.0.2/ a78aabbfdadafcc6fa802f6bf45c832e645bc191 | bzip2 -9 > x11-util-modular-0.0.2.tar.bz2
########################################################################
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2+ and MIT
Requires:	perl
Requires:	sudo
Requires:	git-core
Requires:	cvs
Requires:	make
Requires:	gcc
Requires:	bison
Requires:	flex
Requires:	autoconf
Requires:	glibc-devel
Requires:	pkgconfig(freetype2)
Requires:	strace
Requires:	wget
BuildArch:	noarch

# git-format-patch master..patches
Patch1:		0001-Add-a-set-of-scripts-to-allow-easier-build-of-xorg-l.patch
Patch2:		0002-Update-to-latest-version-of-build-scripts.patch
Patch3:		0003-Update-to-latest-build-scripts.patch
Patch4:		0004-Update-for-rpm-build-and-current-git-master.patch
Patch5:		0005-Update-rpm-build-to-match-Mandriva-cooker.patch
Patch6:		0006-Update-script-to-build-a-xorg-snapshot-and-the-rpm-b.patch
Patch7:		0007-Update-build-scripts-to-match-latest-build-requirem.patch
Patch8:		0008-Update-to-latest-build-of-snapshot-packages.patch

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

pushd xorg-scripts
for script in *.pl; do
	install -D -m 755 $script %{buildroot}/%{_bindir}/$script
done
install -D -m 644 xorg-scripts.txt %{buildroot}/%{_docdir}/%{name}/xorg-scripts.txt
popd

%files
%{_bindir}/*.pl
%doc %{_docdir}/%{name}/*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-11mdv2011.0
+ Revision: 671231
- mass rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-10mdv2011.0
+ Revision: 524369
- rebuilt for 2010.1

* Wed Jul 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.0.2-9mdv2009.0
+ Revision: 256264
- Update to lastest version of scripts used to build the xorg -snapshot packages.

* Wed Jun 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.0.2-8mdv2009.0
+ Revision: 226014
- Update to latest version used to build xorg-snapshot packages.

* Thu Jun 05 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.0.2-7mdv2009.0
+ Revision: 216198
- Update distro package to match scripts used to build last xorg-snapshot
  packages.

* Thu May 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.0.2-6mdv2009.0
+ Revision: 207955
- Update rpm build to match Mandriva cooker.
  Also update versions of packages (version of available tarballs), and
  some build errors that were introduced when making changes to generate
  rpm specs and tarballs.

* Sat May 10 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.0.2-5mdv2009.0
+ Revision: 205353
- Update for rpm build and current git master.

* Thu May 08 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.0.2-4mdv2009.0
+ Revision: 204741
- Update to latest build scripts.
 These were used to generate the initial *-snapshot Mandriva packages.

* Thu Apr 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.0.2-3mdv2009.0
+ Revision: 195026
- Update to latest version of "xorg-scripts".
  The latest version of xorg/util/modular repository is also in the srpm.

* Thu Mar 13 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.0.2-2mdv2008.1
+ Revision: 187572
- Update to latest git master in base tarball and latest build scripts.
- Don't use any scripts for Mandriva Xorg packages build anymore.
  Instead, convert the scripts to work/build latest development code.
- Fix bug in %%setup and install proper perl script to generate dependencies.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.0.2-1mdv2008.1
+ Revision: 151414
- Update to version 0.0.2 of Mandriva scripts. Major difference is new
  way to build dependency information, that now instead of parsing depend
  files, uses strace to trace syscalls while building the packages and
  parse this information to generate dependency files.
- Change x-build.pl package build order to match list generate  by
  x-check-rpm-deps.pl and also add option to automatically install packages
  as they are build.
  Add option to list BuildRequires to x-check-rpm-deps.pl.
  Add some debugging hints to new file README.debugging.
- More consistency check during build of rpm packages.
  Fix a problem in x-check-symbols.pl that could cause it to not list some
  "special case" symbols.
  Rebuild list of dependencies.
- Update support so that scripts should be able to build the dependencies
  datafiles.
- Bug fixes including better help for setting default git-config values,
  fix default git repository, fix some packages that were listed with the
  incorrect prefix, add support for packages without a git repository,
  handle exit code of "bm -l" and don't continue building packages on error,
  add a faster mode to query the package of a file (with a fallback as
  it seens to fail at least for qt3-devel files).
  Fix hash reference in &update, properly handle modules with an empty
  path, fix some problems in the git repository that were commented in
  x-build.pl.
- Add smarter dependencies detection.
  Support to build from svn repository without using anything from the
  git repository.
  Several consistency checks, including things like checking if a tarball
  is really available.
  Add support to not need to add any new files to existing packages. All
  dependency data should be stored in x11-util-modular package, and should
  be done in the next commit of this package.
- Update x-build.pl script for initial support to build from tarballs as
  an alternate build method, as well as possibly generating some specs on
  the fly. Script still not fully functional o completely automatize work
  on X Org releated packages.

* Wed Dec 26 2007 Paulo Andrade <pcpa@mandriva.com.br> 0.0.1-1mdv2008.1
+ Revision: 137992
- Fix some typos. Should be ok to submit. Most things still need a lot of
  user intervention, but x-check-deps.pl should be ok to generate dependencies,
  and enough information to know if a module neeed to be rebuilt or not,
  based on changes on other packages.
- Add initial files to a mandriva specific version of x11-util-modular
  pseudo package (pseudo package because it is only a set of scripts used
  by xorg to generate tarballs).
  This set of scripts, still in a initial version are expected to allow
  automatizing most of the required management to make sure xorg packages
  are functional.
  There are scripts to help checking out the proper version from git
  repository and mandriva svn repository.
  Better documentation should be done to instruct packagers to also
  update git.mandriva.com from anongit.freedesktop.org as any possible
  conflict must be resolved locally, before pushing to git.mandriva.com.
  There is also initial documentation about the scripts, but a summary is:
  o Allow using a ``make'' style dependency tracking by analyzing autotools
  .deps files and building a "global" dependency file
  o Allow inspecting all shared objects, to help preventing runtime crashes
  due to unresolved symbols.
  o Dependency tracking a listing of proper order packages must be built.
- Add ``initial xorg modular'' mandriva specific set of scripts and related
  documentation.

