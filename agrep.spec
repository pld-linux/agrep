Summary:	Approximate grep
Summary(pl):	Wersja grep dopuszczaj±ca b³êdy
Name:		agrep
Version:	2.04
Release:	5
License:	distributable not for profit, free use
Group:		Applications/Text
Source0:	ftp://ftp.cs.arizona.edu/agrep/%{name}-%{version}.tar.Z
# Source0-md5:	abc645404d3926a57c3f5e86a6e89ee9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for fast text searching allowing errors. It's similar to egrep
(or grep or fgrep), but it is much more general and usually faster.

%description -l pl
agrep jest narzêdziem podobnym do grep, ale umo¿liwia przeszukiwanie
przybli¿one.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install agrep $RPM_BUILD_ROOT%{_bindir}/agrep
install agrep.1 $RPM_BUILD_ROOT%{_mandir}/man1/agrep.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README agrep.algorithms agrep.chronicle contribution.list
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
