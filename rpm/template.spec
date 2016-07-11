Name:           ros-indigo-summit-x-gazebo
Version:        1.0.3
Release:        0%{?dist}
Summary:        ROS summit_x_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/summit_x_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-summit-x-control
Requires:       ros-indigo-summit-x-description
Requires:       ros-indigo-summit-x-robot-control
Requires:       ros-indigo-tf
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-gazebo-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-summit-x-control
BuildRequires:  ros-indigo-summit-x-description
BuildRequires:  ros-indigo-summit-x-robot-control
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-xacro

%description
Launch files and world files to start the models in gazebo

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jul 11 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.3-0
- Autogenerated by Bloom

* Mon Jul 11 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.2-0
- Autogenerated by Bloom

* Fri Jul 08 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.1-0
- Autogenerated by Bloom

