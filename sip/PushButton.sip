%Import QtWidgets/QtWidgetsmod.sip

namespace ads
{


class CPushButton : QPushButton
{
    %TypeHeaderCode
    #include <PushButton.h>
    %End
    
public:
    enum Orientation {
        Horizontal,
        VerticalTopToBottom,
        VerticalBottomToTop
    };
    virtual QSize sizeHint() const;
    
    ads::CPushButton::Orientation buttonOrientation() const;
    void setButtonOrientation(ads::CPushButton::Orientation orientation);

};

};
