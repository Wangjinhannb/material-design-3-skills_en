@Entry
@Component
struct Index {
  @State name: string = 'Material User'
  build() {
    Column({ space: 16 }) {
      Text('Classic Material Design 3').fontSize(28).fontWeight(FontWeight.Normal)
      Button('Primary action')
      TextInput({ text: this.name, placeholder: 'Display name' })
        .onChange((value: string) => { this.name = value })
    }.padding(24).width('100%')
  }
}
