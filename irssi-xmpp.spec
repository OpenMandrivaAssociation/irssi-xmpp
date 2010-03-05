Name:		irssi-xmpp
Version:	0.50
Release:	%mkrel 1
Summary:	An irssi Module to Connect to the Jabber Network
Source:		irssi-xmpp-%version.tar.gz
URL:		http://cybione.org/~irssi-xmpp/
Group:		Networking/IRC
License:	GPLv2
BuildRoot:	%{_tmppath}/build-%{name}-%{version}
BuildRequires:	loudmouth-devel irssi-devel >= 0.8.13
BuildRequires:	gcc glibc-devel make
Requires:	irssi >= 0.8.13

%description
irssi-xmpp is a irssi plugin to connect to the jabber network.

%prep
%setup -q -n %{name}-%{version}

%build
export IRSSI_INCLUDE="%{_includedir}/irssi" PREFIX=%{_prefix} IRSSI_LIB=%{_libdir}/irssi IRSSI_DOC=%{_defaultdocdir}
%make

%install
%{__rm} -Rf %{buildroot}
export IRSSI_INCLUDE="%{_includedir}/irssi" PREFIX=%{_prefix} IRSSI_LIB=%{_libdir}/irssi IRSSI_DOC=%{_defaultdocdir}
%makeinstall_std

%clean
%__rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc COPYING NEWS README
%{_libdir}/irssi/modules/libfe_xmpp.so
%{_libdir}/irssi/modules/libxmpp_core.so
%{_libdir}/irssi/modules/libtext_xmpp.so
%{_datadir}/irssi/help/roster
%{_datadir}/irssi/help/xmppconnect
%{_datadir}/irssi/help/xmppserver
