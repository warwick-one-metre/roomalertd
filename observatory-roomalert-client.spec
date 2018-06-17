Name:      observatory-roomalert-client
Version:   2.1.2
Release:   0
Url:       https://github.com/warwick-one-metre/roomalertd
Summary:   Room Alert client for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python34-Pyro4, python34-warwick-observatory-common
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-warwick-observatory-common
%endif
%description
Part of the observatory software for the Warwick La Palma telescopes.

roomalert is a commandline utility that queries the Room Alert daemon.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/roomalert %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/roomalert %{buildroot}/etc/bash_completion.d/roomalert

%files
%defattr(0755,root,root,-)
%{_bindir}/roomalert
/etc/bash_completion.d/roomalert

%changelog
