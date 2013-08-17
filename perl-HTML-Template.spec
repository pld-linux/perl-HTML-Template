#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Template
Summary:	HTML::Template - Perl module to use HTML templates from CGI scripts
Summary(pl.UTF-8):	HTML::Template - moduł Perla do obsługi szablonów HTML w skryptach CGI
Name:		perl-HTML-Template
Version:	2.94
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7b7683c3672d55fb922734ea1e9ba7e8
URL:		https://github.com/mpeters/html-template/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-IPC-SharedCache
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts make using HTML templates simple and natural.

It extends standard HTML with a few new HTML-esque tags - <TMPL_VAR>,
<TMPL_LOOP>, <TMPL_INCLUDE>, <TMPL_IF> and <TMPL_ELSE>.  The file written
with HTML and these new tags is called a template.  It is usually saved
separate from your script - possibly even created by someone else!

Using this module you fill in the values for the variables, loops and
branches declared in the template.  This allows you to seperate design -
the HTML - from the data, which you generate in the Perl script.

%description -l pl.UTF-8
HTML::Template jest modułem pozwalającym na wykorzystywanie szablonów
HTML (i nie tylko) w skryptach CGI (a także w dowolnym innym
oprogramowaniu przy tworzeniu którego zachodzi potrzeba rozdzielenia
programu od wyglądu danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:TEST_SHARED_MEMORY=1 TEST_FILE_CACHE=1 %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/%{pdir}/%{pnam}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README templates scripts
%{perl_vendorlib}/%{pdir}/*.pm
%dir %{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
