%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Template
Summary:	HTML::Template perl module
Summary(pl):	Modu� perla HTML::Template
Name:		perl-HTML-Template
Version:	2.5
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Template - Perl module to use HTML Templates from CGI scripts.

%description -l pl
HTML::Template jest modu�em pozwalaj�cym na wykorzystywanie szablon�w
HTML (i nie tylko) w skryptach CGI (a tak�e w dowolnym innym
oprogramowaniu przy tworzeniu kt�rego zachodzi potrzeba rozdzielenia
programu od wygl�du danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
