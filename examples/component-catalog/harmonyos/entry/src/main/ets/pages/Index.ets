@Entry
@Component
struct Index {
  @State selectedSegment: number = 0
  @State checked: boolean = true
  @State sliderValue: number = 42
  @State searchText: string = ''
  @State fieldText: string = 'Text'

  @Builder
  Section(id: string, title: string, content: () => void) {
    Column({ space: 12 }) {
      Text(title).fontSize(20).fontWeight(FontWeight.Medium)
      Text(id).fontSize(11).fontColor('#49454F')
      content()
    }
    .alignItems(HorizontalAlign.Start)
    .padding(20)
    .width('100%')
    .backgroundColor('#F7F2FA')
    .borderRadius(20)
  }

  build() {
    Scroll() {
      Column({ space: 14 }) {
        Text('Classic Material Design 3').fontSize(14).fontColor('#6750A4')
        Text('Component Catalog').fontSize(32).fontWeight(FontWeight.Medium).margin({ bottom: 8 })

        this.Section('component-buttons', 'Buttons', () => { Row({ space: 8 }) { Button('Filled'); Button('Tonal'); Button('Outlined').type(ButtonType.Normal); Button('Text').type(ButtonType.Normal) }.flexWrap(FlexWrap.Wrap) })
        this.Section('component-floating-action-button', 'Floating action button', () => { Row({ space: 10 }) { Button('+').width(56).height(56).borderRadius(20); Button('＋ New').height(56).borderRadius(20) } })
        this.Section('component-icon-buttons', 'Icon buttons', () => { Row({ space: 10 }) { Button('☆').width(48).height(48).borderRadius(24); Button('★').width(48).height(48).borderRadius(24); Button('⋯').width(48).height(48).borderRadius(24) } })
        this.Section('component-segmented-buttons', 'Segmented buttons', () => { Row() { Button('List').onClick(() => this.selectedSegment = 0); Button('Grid').onClick(() => this.selectedSegment = 1); Button('Compact').onClick(() => this.selectedSegment = 2) } })
        this.Section('component-badges', 'Badges', () => { Row({ space: 14 }) { Text('●').fontColor('#B3261E'); Text('12').fontSize(11).fontColor(Color.White).padding({ left: 7, right: 7, top: 3, bottom: 3 }).backgroundColor('#B3261E').borderRadius(12) } })
        this.Section('component-progress-indicators', 'Progress indicators', () => { Row({ space: 18 }) { Progress({ value: 62, total: 100, type: ProgressType.Linear }).width(220); Progress({ value: 62, total: 100, type: ProgressType.Ring }).width(36).height(36) } })
        this.Section('component-snackbars', 'Snackbar', () => { Row({ space: 20 }) { Text('Settings saved').fontColor(Color.White); Button('Undo').type(ButtonType.Normal) }.padding(14).backgroundColor('#322F35').borderRadius(4) })
        this.Section('component-tooltips', 'Tooltips', () => { Text('Help information').fontSize(12).fontColor(Color.White).padding(8).backgroundColor('#322F35').borderRadius(4) })
        this.Section('component-bottom-sheets', 'Bottom sheet', () => { Button('Open sheet') })
        this.Section('component-cards', 'Cards', () => { Row({ space: 10 }) { Column(){Text('Filled')}.width(140).height(90).padding(14).backgroundColor('#E7E0EC').borderRadius(12); Column(){Text('Outlined')}.width(140).height(90).padding(14).border({width:1,color:'#79747E'}).borderRadius(12) } })
        this.Section('component-carousel', 'Carousel', () => { Row({ space: 10 }) { ForEach([1,2,3,4], (n: number) => { Text(`0${n}`).width(140).height(90).textAlign(TextAlign.Center).backgroundColor('#EADDFF').borderRadius(20) }) }.width('100%') })
        this.Section('component-dialogs', 'Dialogs', () => { Button('Open dialog') })
        this.Section('component-divider', 'Divider', () => { Column({ space: 14 }) { Divider(); Divider().margin({ left: 48 }) }.width('100%') })
        this.Section('component-lists', 'List', () => { List() { ListItem(){Text('Single-line list').padding(12)}; ListItem(){Column(){Text('Two-line list');Text('Supporting text').fontSize(12)}.alignItems(HorizontalAlign.Start).padding(12)} }.height(120).width('100%') })
        this.Section('component-side-sheets', 'Side sheet', () => { Column(){Text('Side sheet').fontWeight(FontWeight.Medium);Text('Supporting information')}.width(260).padding(20).backgroundColor('#E7E0EC').borderRadius(20) })
        this.Section('component-bottom-app-bar', 'Bottom app bar', () => { Row({space:10}){Button('Menu').type(ButtonType.Normal);Button('Search').type(ButtonType.Normal);Blank();Button('+').width(48).height(48).borderRadius(18)}.width('100%') })
        this.Section('component-top-app-bar', 'Top app bar', () => { Row({space:10}){Button('←').type(ButtonType.Normal);Text('Page title').layoutWeight(1);Button('⋯').type(ButtonType.Normal)}.width('100%') })
        this.Section('component-navigation-bar', 'Navigation bar', () => { Row(){Button('Home').layoutWeight(1);Button('Saved').layoutWeight(1);Button('Settings').layoutWeight(1)}.width('100%') })
        this.Section('component-navigation-drawer', 'Navigation drawer', () => { Column(){Button('Inbox').width(220);Button('Drafts').width(220);Button('Archive').width(220)}.alignItems(HorizontalAlign.Start) })
        this.Section('component-navigation-rail', 'Navigation rail', () => { Row({space:10}){Button('Home');Button('Saved');Button('Settings')} })
        this.Section('component-search', 'Search', () => { TextInput({ text: this.searchText, placeholder: 'Search' }).onChange((v: string) => this.searchText = v).width('100%').borderRadius(28) })
        this.Section('component-tabs', 'Tabs', () => { Row(){Button('Overview').layoutWeight(1);Button('Activity').layoutWeight(1);Button('Settings').layoutWeight(1)}.width('100%') })
        this.Section('component-checkbox', 'Checkbox', () => { Row({space:14}){Checkbox({name:'a'});Text('Not selected');Checkbox({name:'b'}).select(true);Text('Selected')} })
        this.Section('component-chips', 'Chips', () => { Row({space:8}){Button('Assist').height(32);Button('Filter').height(32);Button('Input ×').height(32);Button('Suggestion').height(32)}.flexWrap(FlexWrap.Wrap) })
        this.Section('component-date-pickers', 'Date picker', () => { Row({space:10}){TextInput({text:'2026-10-03'}).width(180);Button('Choose date')} })
        this.Section('component-menus', 'Menu', () => { Button('Menu') })
        this.Section('component-radio-button', 'Radio button', () => { Row({space:12}){Radio({value:'system',group:'theme'}).checked(true);Text('System');Radio({value:'light',group:'theme'});Text('Light');Radio({value:'dark',group:'theme'});Text('Dark')} })
        this.Section('component-sliders', 'Slider', () => { Slider({value:this.sliderValue,min:0,max:100,step:1}).onChange((v:number)=>this.sliderValue=v).width(300) })
        this.Section('component-switch', 'Switch', () => { Row({space:12}){Toggle({type:ToggleType.Switch,isOn:this.checked}).onChange((v:boolean)=>this.checked=v);Text('Notifications')} })
        this.Section('component-time-pickers', 'Time picker', () => { TextInput({text:'09:30'}).width(180) })
        this.Section('component-text-fields', 'Text fields', () => { Column({space:10}){TextInput({text:this.fieldText,placeholder:'Filled'}).onChange((v:string)=>this.fieldText=v);TextInput({text:this.fieldText,placeholder:'Outlined'}).onChange((v:string)=>this.fieldText=v).border({width:1,color:'#79747E'})}.width('100%') })
      }
      .padding(20)
      .width('100%')
    }
    .width('100%')
    .height('100%')
  }
}
