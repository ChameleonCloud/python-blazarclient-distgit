%global git_branch chameleoncloud-stable-rocky

Name:           python-blazarclient
Epoch:          1
Summary:        Python client for Blazar
Version:        2.0.0
Release:        2%{?dist}
License:        ASL 2.0
URL:            http://www.openstack.org
Source0:        https://github.com/ChameleonCloud/python-blazarclient/archive/chameleoncloud/stable/rocky/%{name}-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    python2-devel
BuildRequires:    python-pbr
BuildRequires:    python-setuptools

Requires:         python-babel
Requires:         python-cliff
Requires:         python-keystoneclient
Requires:         python-oslo-i18n
Requires:         python-oslo-log
Requires:         python-oslo-utils
Requires:         python-pbr
Requires:         python-prettytable
Requires:         python-requests
Requires:         python-six

%prep
%setup -q -n %{name}-%{git_branch}
rm requirements.txt test-requirements.txt

%build
PBR_VERSION=%{version} %{__python2} setup.py build

%install
PBR_VERSION=%{version} %{__python2} setup.py install --skip-build --root=%{buildroot}

%description
A Python and command line client library for Blazar.

%files
%doc LICENSE README.rst
%{_bindir}/*
%{python2_sitelib}/blazarclient*
%{python2_sitelib}/python_blazarclient*

%changelog
* Tue Jan 8 2019 Pierre Riteau <pierre@stackhpc.com> 1:2.0.0-2
- openstack/python-blazarclient: 6786946cb673885adb6cf2a44f98365061e4fa8c
* Tue Aug 28 2018 Pierre Riteau <priteau@uchicago.edu> 1:2.0.0-1
- Initial packaging for Rocky
