%include	/usr/lib/rpm/macros.perl
Summary:	HTML-Template perl module
Summary(pl):	Modu³ perla HTML-Template
Name:		perl-HTML-Template
Version:	2.0
Release:	1
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Vendor: PLD
Distribution: PLD
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Template-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/buildroot-%{name}-%{version}

%description
HTML-Template - Perl module to use HTML Templates from CGI scripts.

%description -l pl
HTML-Template  jest modu³em  pozwalaj±cym na wykorzystywanie  szablonów HTML
(i nie tylko) w skryptach CGI (a tak¿e w dowolnym innym  oprogramowaniu przy
tworzeniu którego zachodzi potrzeba rozdzielenia programu od wygl±du danych.

%prep
%setup -q -n HTML-Template-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/Template
  sed -e "s#$RPM_BUILD_ROOT##" .packlist | sort | uniq >.packlist.new
  mv .packlist.new .packlist
	
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,ANNOUNCE}.gz templates scripts

%{perl_sitelib}/HTML/Template.pm
%{perl_sitearch}/auto/HTML/Template

%{_mandir}/man3/*
