Name:		irssi-xmpp
Version:	0.52
Release:	2
Summary:	An irssi Module to Connect to the Jabber Network
Source0:	%name-%version.tar.gz
URL:		https://cybione.org/~irssi-xmpp/
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


%changelog
* Tue Mar 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.52-1
+ Revision: 784680
- version update 0.52

* Tue May 24 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.51-1
+ Revision: 678192
- new version 0.51

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri Mar 05 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.50-1mdv2010.1
+ Revision: 514433
- Rewrite parts of spec, not use CVS.
- update to O.50
- fix source to use tar.gz (fix %%prep too)

* Tue May 19 2009 Nicolas Vigier <nvigier@mandriva.com> 0.13-4.cvs20090519.1mdv2010.0
+ Revision: 377580
- update to cvs version (much more stable than the outdated stable version, and recommended on website)
- fix license and indentation
- update URL

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.13-3mdv2009.0
+ Revision: 247277
- rebuild

* Mon Feb 11 2008 Olivier Thauvin <nanardon@mandriva.org> 0.13-1mdv2008.1
+ Revision: 165626
- import irssi-xmpp

