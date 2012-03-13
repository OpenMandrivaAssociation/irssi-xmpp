Name:		irssi-xmpp
Version:	0.52
Release:	1
Summary:	An irssi Module to Connect to the Jabber Network
Source0:	%name-%version.tar.gz
URL:		http://cybione.org/~irssi-xmpp/
Group:		Networking/IRC
License:	GPLv2
BuildRequires:	loudmouth-devel irssi-devel >= 0.8.13
BuildRequires:	gcc glibc-devel make
Requires:	irssi >= 0.8.13

%description
irssi-xmpp is a irssi plugin to connect to the jabber network.

%prep
%setup -q

%build
export IRSSI_INCLUDE="%{_includedir}/irssi" PREFIX=%{_prefix} IRSSI_LIB=%{_libdir}/irssi IRSSI_DOC=%{_defaultdocdir}
%make

%install
export IRSSI_INCLUDE="%{_includedir}/irssi" PREFIX=%{_prefix} IRSSI_LIB=%{_libdir}/irssi IRSSI_DOC=%{_defaultdocdir}
%makeinstall_std

%files
%doc COPYING NEWS README
%{_libdir}/irssi/modules/libfe_xmpp.so
%{_libdir}/irssi/modules/libxmpp_core.so
%{_libdir}/irssi/modules/libtext_xmpp.so
%{_datadir}/irssi/help/roster
%{_datadir}/irssi/help/xmppconnect
%{_datadir}/irssi/help/xmppserver
