#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "tokens" / "source"
OUT = ROOT / "tokens" / "generated"

def load(name): return json.loads((SRC/name).read_text(encoding="utf-8"))
def color_hex(token):
    ext=token.get("$extensions",{}).get("org.md3-cross-platform",{})
    if "hex" in ext: return ext["hex"].upper()
    v=token["$value"]; vals=[round(float(x)*255) for x in v["components"]]; a=round(float(v.get("alpha",1))*255)
    h="#"+"".join(f"{x:02X}" for x in vals)
    return h if a==255 else h+f"{a:02X}"
def colors(name):
    d=load(name); return {k:color_hex(v) for k,v in d["color"].items() if not k.startswith("$")}
def kebab(s):
    out=[]
    for ch in s: out.extend(["-",ch.lower()]) if ch.isupper() else out.append(ch)
    return "".join(out)
def pascal(s): return s[0].upper()+s[1:]
def write(p,s): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s.rstrip()+"\n",encoding="utf-8")

light,dark=colors("color-light.tokens.json"),colors("color-dark.tokens.json")
type_data=load("typography.tokens.json"); shape=load("shape.tokens.json")["corner"]
elev=load("elevation.tokens.json")["levels"]; state=load("state.tokens.json"); motion=load("motion.tokens.json")

# Web
css=[":root {"]
for k,v in light.items(): css.append(f"  --md-sys-color-{kebab(k)}: {v};")
for k,v in shape.items(): css.append(f"  --md-sys-shape-corner-{kebab(k)}: {'9999px' if k=='full' else str(v)+'px'};")
for k,v in elev.items(): css.append(f"  --md-sys-elevation-{kebab(k)}: {v}px;")
for k,v in state["stateLayerOpacity"].items(): css.append(f"  --md-sys-state-{kebab(k)}-opacity: {v};")
for k,v in state["disabled"].items(): css.append(f"  --md-sys-state-disabled-{kebab(k)}: {v};")
for k,v in motion["durationMs"].items(): css.append(f"  --md-sys-motion-duration-{kebab(k)}: {v}ms;")
for k,v in motion["easing"].items(): css.append(f"  --md-sys-motion-easing-{kebab(k)}: cubic-bezier({', '.join(str(x) for x in v)});")
for role,v in type_data["roles"].items():
    r=kebab(role); css += [f"  --md-sys-typescale-{r}-size: {v['fontSize']}px;",f"  --md-sys-typescale-{r}-line-height: {v['lineHeight']}px;",f"  --md-sys-typescale-{r}-weight: {v['fontWeight']};",f"  --md-sys-typescale-{r}-tracking: {v['letterSpacing']}px;"]
css.append("}"); css.append(':root[data-theme="dark"] {')
for k,v in dark.items(): css.append(f"  --md-sys-color-{kebab(k)}: {v};")
css.append("}"); css.append('@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {')
for k,v in dark.items(): css.append(f"  --md-sys-color-{kebab(k)}: {v};")
css.append("} }")
write(OUT/"web/tokens.css","\n".join(css))

# Android Kotlin metrics + colors
kt=["package org.example.md3tokens","","import androidx.compose.ui.graphics.Color","import androidx.compose.ui.unit.dp","import androidx.compose.ui.unit.sp","","object Md3ReferenceColors {"]
for prefix,data in [("Light",light),("Dark",dark)]:
    for k,v in data.items(): kt.append(f"    val {prefix}{pascal(k)} = Color(0xFF{v[1:7]})")
kt += ["}","","object Md3Metrics {"]
for k,v in shape.items(): kt.append(f"    val Shape{pascal(k)} = {v if k!='full' else 9999}.dp")
for k,v in elev.items(): kt.append(f"    val Elevation{pascal(k)} = {v}.dp")
for role,v in type_data["roles"].items(): kt += [f"    val Type{pascal(role)}Size = {v['fontSize']}.sp",f"    val Type{pascal(role)}LineHeight = {v['lineHeight']}.sp"]
for k,v in motion["durationMs"].items(): kt.append(f"    const val Motion{pascal(k)}Ms: Int = {v}")
kt.append("}")
write(OUT/"android/MaterialTokens.kt","\n".join(kt))

# HarmonyOS
ets=["// Generated reference tokens. Do not edit directly.","export class Md3ReferenceTokens {"]
for prefix,data in [("light",light),("dark",dark)]:
    for k,v in data.items(): ets.append(f"  static readonly {prefix}{pascal(k)}: string = '{v}';")
for k,v in shape.items(): ets.append(f"  static readonly shape{pascal(k)}: number = {v if k!='full' else 9999};")
for k,v in elev.items(): ets.append(f"  static readonly elevation{pascal(k)}: number = {v};")
for k,v in motion["durationMs"].items(): ets.append(f"  static readonly motion{pascal(k)}Ms: number = {v};")
ets.append("}")
write(OUT/"harmonyos/MaterialTokens.ets","\n".join(ets))

# Swift
sw=["import SwiftUI","","enum Md3ReferenceTokens {"]
for prefix,data in [("light",light),("dark",dark)]:
    for k,v in data.items(): sw.append(f"    static let {prefix}{pascal(k)} = Color(hex: \"{v}\")")
for k,v in shape.items(): sw.append(f"    static let shape{pascal(k)}: CGFloat = {v if k!='full' else 9999}")
for k,v in elev.items(): sw.append(f"    static let elevation{pascal(k)}: CGFloat = {v}")
for k,v in motion["durationMs"].items(): sw.append(f"    static let motion{pascal(k)}Seconds: Double = {v/1000:.3f}")
sw += ["}","","extension Color {","    init(hex: String) {","        let clean = hex.trimmingCharacters(in: CharacterSet(charactersIn: \"#\"))","        let value = UInt64(clean, radix: 16) ?? 0","        let r = Double((value >> 16) & 0xFF) / 255","        let g = Double((value >> 8) & 0xFF) / 255","        let b = Double(value & 0xFF) / 255","        self.init(red: r, green: g, blue: b)","    }","}"]
write(OUT/"ios/MaterialTokens.swift","\n".join(sw))

# Windows XAML
x=["<ResourceDictionary","    xmlns=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"","    xmlns:x=\"http://schemas.microsoft.com/winfx/2006/xaml\">","  <ResourceDictionary.ThemeDictionaries>","    <ResourceDictionary x:Key=\"Light\">"]
for k,v in light.items(): x.append(f"      <Color x:Key=\"Md3Color{pascal(k)}\">{v}</Color>")
x += ["    </ResourceDictionary>","    <ResourceDictionary x:Key=\"Dark\">"]
for k,v in dark.items(): x.append(f"      <Color x:Key=\"Md3Color{pascal(k)}\">{v}</Color>")
x += ["    </ResourceDictionary>","  </ResourceDictionary.ThemeDictionaries>"]
for k,v in shape.items(): x.append(f"  <x:Double x:Key=\"Md3Shape{pascal(k)}\">{v if k!='full' else 9999}</x:Double>")
for k,v in elev.items(): x.append(f"  <x:Double x:Key=\"Md3Elevation{pascal(k)}\">{v}</x:Double>")
x.append("</ResourceDictionary>")
write(OUT/"windows/MaterialTokens.xaml","\n".join(x))

# GTK CSS
css=[":root {"]
for k,v in light.items(): css.append(f"  --md-sys-color-{kebab(k)}: {v};")
for k,v in shape.items(): css.append(f"  --md-sys-shape-corner-{kebab(k)}: {'9999px' if k=='full' else str(v)+'px'};")
for k,v in motion["durationMs"].items(): css.append(f"  --md-sys-motion-duration-{kebab(k)}: {v}ms;")
css.append("}"); css.append(".dark {")
for k,v in dark.items(): css.append(f"  --md-sys-color-{kebab(k)}: {v};")
css.append("}")
write(OUT/"linux-gtk/md3-tokens.css","\n".join(css))

# QML
qml=["pragma Singleton","import QtQuick","","QtObject {"]
for prefix,data in [("light",light),("dark",dark)]:
    for k,v in data.items(): qml.append(f"    readonly property color {prefix}{pascal(k)}: \"{v}\"")
for k,v in shape.items(): qml.append(f"    readonly property real shape{pascal(k)}: {v if k!='full' else 9999}")
for k,v in motion["durationMs"].items(): qml.append(f"    readonly property int motion{pascal(k)}Ms: {v}")
qml.append("}")
write(OUT/"linux-qt/MaterialTokens.qml","\n".join(qml))
print("Generated platform tokens in",OUT)
