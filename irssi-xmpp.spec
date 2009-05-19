Name:		irssi-xmpp
Version:	0.13
Release:	%mkrel 3
Summary:	An irssi Module to Connect to the Jabber Network
Source:		http://cybione.org/src/irssi-xmpp/irssi-xmpp-%{version}.tar.gz
URL:		http://cybione.org/~irssi-xmpp/
Group:		Networking/IRC
License:	GPLv2
BuildRoot:	%{_tmppath}/build-%{name}-%{version}
BuildRequires:	loudmouth-devel irssi-devel
BuildRequires:	gcc glibc-devel make

%description
irssi-xmpp is a irssi plugin to connect to the jabber network.

%prep
%setup -q

%build
export IRSSI_INCLUDE="%{_includedir}/irssi"
%make

%install
%__install -d %{buildroot}%{_libdir}/irssi/modules
%__install -m0755 \
			  src/fe-common/libfe_xmpp.so \
			  src/core/libxmpp_core.so \
			  %{buildroot}%{_libdir}/irssi/modules/

%clean
%__rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc COPYING NEWS README TODO
%{_libdir}/irssi/modules/libfe_xmpp.so
%{_libdir}/irssi/modules/libxmpp_core.so
