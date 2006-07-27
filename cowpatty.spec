
Summary:	coWPAtty is designed to audit the security of pre-shared keys selected in WiFi Protected Access (WPA) networks
Summary(pl):	coWPAtty zosta³ stworzony do badania zabezpieczeñ kluczy PSK zabranych z sieci szyfrowaych metod± WPA.
Name:		cowpatty
Version:	2.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/cowpatty/%{name}-%{version}.tgz
# Source0-md5:	3e84ea75ea014381b1c77a824714bdde
URL:		http://cowpatty.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
coWPAtty is designed to audit the security of pre-shared keys selected
in WiFi Protected Access (WPA) networks.

%description -l pl
coWPAtty zosta³ stworzony do badania zabezpieczeñ kluczy PSK zabranych
z sieci szyfrowaych metod± WPA.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install cowpatty $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG COPYING FAQ README TODO WISHLIST
%attr(755,root,root) %{_bindir}/cowpatty
