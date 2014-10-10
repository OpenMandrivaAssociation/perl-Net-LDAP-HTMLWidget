%define upstream_name    Net-LDAP-HTMLWidget
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Like FromForm but with Net::LDAP and HTML::Widget
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%upstream_name/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MR/MRAMBERG/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBIx::Class::HTMLWidget)
BuildArch:	noarch

%description
Something like Class::DBI::FromForm / Class::DBI::FromCGI but using
HTML::Widget for form creation and validation and Net::LDAP.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Net/LDAP/HTMLWidget.pm
%{_mandir}/*/*


%changelog
* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 408966
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-4mdv2009.0
+ Revision: 258053
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-3mdv2009.0
+ Revision: 246152
- rebuild

* Mon Feb 25 2008 Buchan Milne <bgmilne@mandriva.org> 0.07-1mdv2008.1
+ Revision: 174899
- import perl-Net-LDAP-HTMLWidget


* Tue Feb 19 2008 Buchan Milne <bgmilne@mandriva.org> 0.07-1
- Update to 0.07 and introduce in Mandriva

* Thu Jun 28 2007 Dzunani Chavalala <dzunani@staff.telkomsa.net>
- Build version 0.01
