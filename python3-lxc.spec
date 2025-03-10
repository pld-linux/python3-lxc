Summary:	Python 3 bindings for LXC
Summary(pl.UTF-8):	Wiązania Pythona 3 do LXC
Name:		python3-lxc
Version:	5.0.0
Release:	2
License:	LGPL v2.1+
Group:		Libraries/Python
#Source0:	https://files.pythonhosted.org/packages/source/l/lxc/lxc-%{version}.tar.gz
#Source0Download: https://linuxcontainers.org/lxc/downloads/
Source0:	https://linuxcontainers.org/downloads/lxc/%{name}-%{version}.tar.gz
# Source0-md5:	99e303f464d943dda09680976a9c4a84
URL:		https://pypi.org/project/lxc/
BuildRequires:	lxc-devel >= 5.0.0
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	lxc-libs >= 5.0.0
Requires:	python3-modules >= 1:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains LXC bindings for Python 3.

%description -l pl.UTF-8
Ten pakiet zawiera wiązania LXC dla Pythona 3.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' examples/*.py

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{py3_sitedir}/_lxc.cpython-*.so
%{py3_sitedir}/lxc
%{py3_sitedir}/python3_lxc-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
