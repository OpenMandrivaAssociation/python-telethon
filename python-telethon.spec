%define module Telethon

Name:           python-telethon
Version:        1.23.0
Release:        1
Summary:        Full-featured Telegram client library for Python 3
License:        MIT
Group:          Development/Python
URL:            https://github.com/LonamiWebs/Telethon
Source0:        https://pypi.python.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pyaes)
BuildRequires:  python3dist(rsa)
%{?python_provide:%python_provide python3-%{module}}
  
Requires: python3dist(pyaes)
Requires: python3dist(rsa)

%description
Telethon is an asyncio Python 3 MTProto library to interact with Telegram's API as a user or through a bot account (bot API alternative).

#--------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
%autopatch -p1

# drop bundled egg-info
rm -rf *.egg-info/

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/%{module}*
%{python_sitelib}/telethon
