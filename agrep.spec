Summary:	Approximate grep
Summary(pl):	Wersja grep dopuszczaj±ca b³êdy
Name:		agrep
Version:	2.04
Release:	5
License:	distributable not for profit, free use
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	ftp://ftp.cs.arizona.edu/agrep/%{name}-%{version}.tar.Z
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

gzip -9nf COPYRIGHT README agrep.algorithms agrep.chronicle contribution.list

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
