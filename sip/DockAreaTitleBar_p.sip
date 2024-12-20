%Import QtWidgets/QtWidgetsmod.sip

namespace ads
{

class CSpacerWidget : QWidget
{
    %TypeHeaderCode
    #include <DockAreaTitleBar_p.h>
    %End

public:
	CSpacerWidget(QWidget* Parent /TransferThis/ = 0 );
	virtual QSize sizeHint() const;
	virtual QSize minimumSizeHint() const;
};

};
