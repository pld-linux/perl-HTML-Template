%include	/usr/lib/rpm/macros.perl
Summary:	HTML-Template perl module
Summary(pl):	Modu³ perla HTML-Template
Name:		perl-HTML-Template
Version:	2.2
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Template-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-Template - Perl module to use HTML Templates from CGI scripts.

%description -l pl
HTML-Template jest modu³em pozwalaj±cym na wykorzystywanie szablonów
HTML (i nie tylko) w skryptach CGI (a tak¿e w dowolnym innym
oprogramowaniu przy tworzeniu którego zachodzi potrzeba rozdzielenia
programu od wygl±du danych.

%prep
%setup -q -n HTML-Template-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz templates scripts
%{perl_sitelib}/HTML/Template.pm
%{_mandir}/man3/*
