namespace ads
{

class CDockComponentsFactory
{
%TypeHeaderCode
#include <DockComponentsFactory.h>
%End

public:
  virtual ~CDockComponentsFactory();
  virtual CDockWidgetTab* createDockWidgetTab(CDockWidget* DockWidget /Transfer/) const;
  virtual CAutoHideTab* createDockWidgetSideTab(CDockWidget* DockWidget /Transfer/) const;
  virtual CDockAreaTabBar* createDockAreaTabBar(CDockAreaWidget* DockArea /Transfer/) const;
  virtual CDockAreaTitleBar* createDockAreaTitleBar(CDockAreaWidget* DockArea /Transfer/) const;
  static const CDockComponentsFactory* factory();
%MethodCode
    QSharedPointer<ads::CDockComponentsFactory> *grab;

    Py_BEGIN_ALLOW_THREADS
    // This will leak but there seems to be no way to detach the object.
    grab = new QSharedPointer<ads::CDockComponentsFactory>(ads::CDockComponentsFactory::factory());
    Py_END_ALLOW_THREADS

    sipRes = grab->data();
%End
  static void setFactory(CDockComponentsFactory* Factory /KeepReference/);
  static void resetDefaultFactory();
};

};
