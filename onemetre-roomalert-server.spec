Name:      onemetre-roomalert-server
Version:   2.0.2
Release:   0
Url:       https://github.com/warwick-one-metre/roomalertd
Summary:   Room Alert daemon for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python34-Pyro4, python34-demjson, python34-warwick-observatory-common, observatory-log-client, %{?systemd_requires}
BuildRequires: systemd-rpm-macros
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-demjson, python34-warwick-observatory-common, observatory-log-client, %{?systemd_requires}
%endif

%description
Part of the observatory software for the Warwick one-meter telescope.

roomalertd is a Pyro frontend for querying the Room Alert via http.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/roomalertd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/roomalertd.service %{buildroot}%{_unitdir}

%pre
%if 0%{?suse_version}
%service_add_pre roomalertd.service
%endif

%post
%if 0%{?suse_version}
%service_add_post roomalertd.service
%endif
%if 0%{?centos_ver}
%systemd_post roomalertd.service
%endif

%preun
%if 0%{?suse_version}
%stop_on_removal roomalertd.service
%service_del_preun roomalertd.service
%endif
%if 0%{?centos_ver}
%systemd_preun roomalertd.service
%endif

%postun
%if 0%{?suse_version}
%restart_on_update roomalertd.service
%service_del_postun roomalertd.service
%endif
%if 0%{?centos_ver}
%systemd_postun_with_restart roomalertd.service
%endif

%files
%defattr(0755,root,root,-)
%{_bindir}/roomalertd
%defattr(-,root,root,-)
%{_unitdir}/roomalertd.service

%changelog