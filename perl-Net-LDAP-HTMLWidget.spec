%define upstream_name    Net-LDAP-HTMLWidget
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Like FromForm but with Net::LDAP and HTML::Widget
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%upstream_name/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MR/MRAMBERG/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel >= 0:5.600
%endif
BuildRequires:	perl(DBIx::Class::HTMLWidget)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Something like Class::DBI::FromForm / Class::DBI::FromCGI but using
HTML::Widget for form creation and validation and Net::LDAP.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Net/LDAP/HTMLWidget.pm
%{_mandir}/*/*
