%global goipath         github.com/xdg/stringprep
%global commit          73f8eece6fdcd902c185bf651de50f3828bed5ed

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Provides an implementation of the stringprep algorithm (RFC-3454)
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/text/unicode/norm)

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup


%install
%goinstall


%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Wed Nov 28 2018 mskalick@redhat.com - 0-0.2.20181127git73f8eec
- Fix issues found during package review

* Tue Nov 27 2018 mskalick@redhat.com - 0-0.1.20181127git73f8eec
- First package for Fedora

