%global packname  siatclust
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.5
Release:          2
Summary:          Shenzhen Institutes of Advanced Technology Clustering Suite
Group:            Sciences/Mathematics
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-lattice R-latticeExtra R-clv
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-lattice R-latticeExtra R-clv

%description
A collection of cluster analysis tools and algorithms for data mining
developed at the Shenzhen Institutes of Advanced Technology (SIAT) under
the Senior International Scientist program of the Chinese Academy of
Sciences. Development of this package is also supported by the Shenzhen
High Technology Development Fund within the Shenzhen Key Laboratory for
High Performance Data Mining.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
