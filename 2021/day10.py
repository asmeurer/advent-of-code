test_input = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

input = """
<{[[({([{<[[([()<>]<<><>>)<[[]()]{<>()}>][<(()[])<()<>>>]]<(<(<><>)(())>)[<([]()){<><>}>{{()<>}<{}>}]>>[({
<<({<{{{[(<{([{}{}]{{}[]}){({}())}}<<[[][]](()<>)>[{<><>}<{}<>>]>>(<[[()]([]{})]((()<>)[()()
({<<({[<[[<[([()])]<<<{}<>><()[]>>[[()<>]<[]()>]>>([((()[])[()])]{[[()()]<<><>>][{<>[]}(()<>)]})
(([[<<[{(({{{(()<>)[()()]}[({}<>)[[][]]]}([{{}<>}<[]()}]{[[][]][()<>]})})(([({[]{}}{[][]})
({{<[[<<{{[{[<{}{}>{[]{}}]<([]{}){()[]}>}]<{([<><>]([]<>)){({}())({}<>)}}[[<{}<>>([]{})][[()[]]]]>}}>>]]
[(<<<{([[[<{(<()<>>{<><>})(<[]<>>([][]))}[<[{}[]]>{<[]>(<><>)}]>([{{[]()}{[]()}}([<>[]][{}<>
<[{[{{([<(<{{[{}<>]({}{})}{{<>[]}(()())}}(<<<>{}>(<><>)>(<<>{}>[[]<>]))>)>[{[<[[()<>]{{}<>
{(<<[([<{<<<({()()}(<><>)}{((){})([]())}>>[<{<[]<>>{[]{}}}([()()])>]>}>]{{([{<{{[]<>}(<>)}<({}(
((<[{(({([<{(<[][]>)[<<>{}><()<>>]}<{<{}{}>}[{()[]}<{}[]>]>>])})<[{[{([{[]()}((){})][<<>()><()()>])>]}][[({{[
[[{([[<<[({[<<[]{}>{[][]}>(<()<>>[{}()])][([{}[]}[<><>]){[{}()]}]}[<<<{}<>>{()<>}>(<{}()>([]()))>{[[<><>][
{{{<[([[{<[<{([]{}>{<>()}}{<(){}><()()>}>[{[[][]](<>())}[{[]<>}[<>[]]]]]{<{{{}[]}{<><>}}[[()()](<
(([{(({[[[[{(<<>[]>((){})){<()<>><[]{}>}}{[{{}()}(()[])]((()){()<>})}]]]<[<<{(()[])<{}[]>}{
{<<([(<([{{(<(()<>)[[][]]>{[[]{}]{(){}}})[{<(){}>[[]<>]}]}}])[[[([[{()()}{<>[]}]{[()]{[][]}}]<[((
[{<<{<([(<[<{<{}[]>{{}[]}}(([]()))>{([(){}]<()[]>)(<[][]>{[]<>})}]>[{<<{<>()}[{}[]]>{(<><>)}>{[<[]<>>{()[]}]<
<{{<{[[{{([({<()>{(){}}}((<>[])(<><>)))[(<[]<>>[()[]])<<()()>{<>{}}>]])<[{[{[]<>}{()()}][[{}{}]<[]>]}<{{{
[(<[{([{({<<[<<>()>[[]()]]{<<>{}><{}<>>}><{<()()>{{}{}}}(({}<>)<()<>>)>>})({(([<{}<>>{[][]
{(([{[<{{[({{[{}<>][()]}<{{}<>}>}(({<>[]})))]{((<[<>{}][<>[])>[[<>()]{[][]}]))<<<({}<>){{}<>}>(
{[<{({((([[{[(<>{}){<>()}][([]{}}]}]{[<(()()){[]()}>((<>[])<(){}>)]}]){<(<<{{}<>}>>)([[{<><>}<
{<{[(<{<[({<<[<><>]{()()}>[{()<>}<{}>]>[[<[]>][{()[]}{()}]]}(<(({}()){<><>})<(()())[<>()]>>{
<[({[[{<([[{<{{}}>(<<><>>{[]()}}}[{{<>{}}<()<>>}{[[][]]{[]<>}}]]<((([][])<<>{}>)<((){})[{}()
{{[{<[{<<{<<(<{}[]><(){}>)<{<>[]}[{}()]>>[{{[]<>}<()<>>}[{{}<>}(<>())]]><[(({}<>)({}<>))<<{}<>><<
{<<({(<[(<[[{{[][]}{{}}}<[[]()]<<>())>]](<{{{}<>}{()<>}}>)>)]<(({{[[[][]]]}<[[(){}]<[]{}>]>}))>
({{([<<{[(<<{{<>()}<[]()>}<{(){}}{{}{}}>><(<{}[]>{<>{}})<([]<>)([]())>>>)]}>>[[{<{[<<(<>{})
<{({{({<<[{<<{<>}{{}[]}>>[[{[]<>}{()()}]<<[][]>(()())>]}]{<<{[(){}><<><>>}{{<>[]}(()<>)}>[<<(){}>[[]
<({<([[[([({<{(){}}([][])>}<[{[][]}{<>()}]<[(){}][{}<>]>>){<({{}()}{[]{}})>{[{[]{})[()[]]]<[
{([({[(([<{((({}()){{}<>})(<()[]>{()()})){[({}{})<<>[]>]([{}][()])}}>]{<<[<[[][]]{[][]}>({[]{}}<{}()>)
<<{[<({[(<[({<{}{}><()()>})]{<<[<><>]>>}>){{[((<<><>><{}[]>)){<{[]()}(<>())>}]{{{({}<>){[]<>}}{{
<<({<[{(([{({({}())(<>{})}{((){})})[<[[][]]([][])>]}<<[[<>{}][[]<>]]<([]<>)[()()]>><<<{}[]>(()())>>]])[[[
[{<({<(({([([{[]}]<{[]()}[()<>]>]{{(()())<{}()>}{{[]()}<()<>>}}][{(<[]<>>[<>{}])[<[]<>><<><>>]}<(<<
<{{((<<(<{({<{<>{}}[[]{}]>})[[{{[][]}{{}<>}}]]}[(([(()[])<()<>>]((<>[])<<>{}>))<[[<>()][<>
{[([<<<({[{<<[<>{}]<[]<>>>>({<<>{}>((){})}<{[][]}{[]{}}>)}<{(([]{})<<>>><{{}()}(<><>)>}<{<[]
<({[[{{{([(({[{}<>]{[]<>}}[{()<>}<(){}>])<[<{}()>[[]<>]]>)]{{[<{<>()}[{}()]><<<><>>{[][]}>]([[[][]](<>())
[<<{{<[[{[<(<{()[]}[(){}]><[()[]]<<>{}>>)>[[[[[]{}]{[][]}]{<[]{}><(){}>}]({{<>()}<<>{}>}({()<>
[<[[(<[[[[<<<{()<>}[[]()]>>{[[<>[]]{[]{}}]{[<>[]][[]<>]}}>]]({[({[<><>]<{}<>>}<<(){}>[{}()]>)[[<<>
<{{({<([{({({{{}()}((){})})([([][])[[]<>]](([])[{}<>]))}<(([()<>][()[]])[<[]><{}{}>])<{({}<>)<<>()>}
{<[[[([{[<<(({{}<>})(<{}()](<>{}))){[[<>[]]({}<>)]}><[((<>()){[][]})[({}())<{}<>>]]<({<>[]}{{}<>
{<[<[({<({(<(({}[])<{}>)((<>[])({}<>))><(([][])(()()))>)})({{({{<>())}<{<>()}([]{})>)[[(()<>)<<>[]>](<<
{(<(<<{{({{<{(<>[])[[]]}{(<>{})>>{<(()())[{}{}]>{{[]{}}{{}<>}}}}(<{[{}[]]<(){}>}[[{}{}]{()<>}]>([{<>{}}[<>]]
[{[{{[[[{([<(({}{})<[][]>)<([]{})<<>{}>>>[{[[]{}]([]<>)}{(()())[<>[]]}}]((<([]<>)[()<>]>(<{}()>)){<[<>[]](
{<<<<{(({<<({(()())(<>{})}<([][])[[]()]>)[{{[]()}(<>)}]><{[<<>()>]{<[]()>[[]<>]}}>>}>[(<<<[{()<>}{{}<>
[{[(<[<{<[({[{[]<>}<[][]>]{{<>()}}}[({<>[]}{{}{}}){[[]<>](<><>)}])({({{}<>}<{}<>>)}<[((){})[{
{<[[{[(((<({([[]<>](()<>))}[{{()<>}({}())}(<[]{}>{[]{}})])<<(({})[{}{}])[(<>{})<()>]>>>))<[{{<[{{}<>}[[][]
[[<<([{<{((([<{}{}>(<><>)][({}[])])[[(<>{}){{}<>}](<()[]>[[]()])])[{({()}{{}{}})(({}())([]{}))}({[{}[]]{
<<((<[<(([<{[<{}<>>][<{}{}>{{}[]}]}[{<<>()>[[]{}]}{[()[]]([]{})}]><{({()()}{[]})<{[]()}[{}{}]>}{((<>(
({<<{[(({{<<{[[]()]{{}()}}{[<>{}]<[][]>}>{(([]())[<>[]]){<[]{}>{<><>}}}>{{{{<>[]}{{}()]}{{<>{}}[{}{}
{((<<{<<<((<(({}{})(()))[[()()]{{}<>}]>{(<()[]][{}[]])[[<>[]]<<>>]}))>([[{({()[]}{()[]})(<[][]><{}{}>)}[[[[][
[(<<{<[(<([<(<[]()><()()>)>]{({[<><>]{[][]}})}}<[([(()())[{}]]<<(){}>[<><>]>)][<<((){})>>[[{<><>}[{}()]][([]
[<{[<[[(({{{[<{}[]><<>{}}][[{}<>]<<>()>]}{[{[]}[{}[]]]{[()[]]<{}<>>}}}[({<(){}>{{}{}}}<(()[])(
<{([{(<[<<<<[[{}{}]([])](<{}{}>[[][]])>{{(()[]){<>[]}}<[<><>][(){}]>}>(([[{}{}]{{}<>}](<()()>))<<(<>{})<<
[(<[[[[(({[<<<<>{}><<><>>>>]<{[{{}<>}<()>]{{[]{}}[<>[]]}}<<<()[]>([]<>)><(<>{}){[]()}>>>}))[[([{<
[([(({<{([<[({{}{}}<{}{}>)[[[]{}]({}<>)]]<[([]<>)({}[])]{(()[]){[]<>}}>>{[<{[]<>}>{[()[]]<()<>>}][<([
{<[<[[<[{({{<[[]()][{}()]>({()[]}(()[]))}([[<>()]])})}{{<{{[<>]<[]()>}{<{}[]]}}<{{()[]}<[]<>>}([()()]<{}()>)>
[{{(<(([([((<{{}{}}({}())>{{<>[]}<[]{}>})([{<>()}{{}<>}]{<()<>>[{}{}]})>]{{[<(<>){[]{}}>{<<>[]>[()[]]}]
[<<(({[[({({[{[]{}}<<>[]]]{[()()]<<>()>}}{[{<>[]}<()>]}){{<<()[]>{[]{}}><<<>>[[]()]>}}})<[{{[<
<([{{{(<{{{<<({}()){(){})>{<{}{}>{<>()}}>{(<()[]>({}()))<({}())<()()>>}}[(({[]{}}[<>{}])([{}<>])){{{{}}(<
<<{[{[[<([[<(<{}<>><()[]>)<{<>()>[<>()]>>]][{{{{()<>}<{}[]>}[<[]()>[()[]]]}<{[{}](<>{})}>}[<[[<><>]<
[{[([{<<[([[{<<>[]>(<>())}((()())({}{}))>{[({}())<<>()>]<(<><>){()<>}>}]({([(){}]<[]<>>){<[
[{<<[[<((({[<[[]()]>(<<>>(<>{}))]<<([]<>)[<>{}]>{<[][]>(<>())}>}(([{{}<>}{{}[]}]{[()[]]{{}{}}})<
([<<{[([[<{<{({}())}{(()<>)}>[<[{}<>][[]()]><[<>{}]({}[])>]}<[([<>()]){[()<>]([]{})}][[[{}[]]][
<{[[{({<{(<[[(()[])<<>[]>]<<<>()>{[]<>}>]>{[<(<>()){<>[]}>(([][]))]([<[]<>><{}{}>]([<>{}](()()
{[([{{(([[<{<[{}<>]([]{})>[((){})<()[]>]}[[{{}<>}<[][]>]<{[]<>}([]())>]>{<{{{}<>}{(){}}]{{[]
[{{<[([<{[[({[{}[]][(){}]}<{<>()}<[]{}>>)]<<({()<>}[[]()]){[<>[]]<()()>}>>]{[<<(<>[])<[]<>>
<[{<[<((<({[{[{}[])(<>{})}(({}[])[<>])]})>[[([{((){})<<>>}])[<((()<>)[{}{}])[[(){}]]>{<<{}()>{
({[[[[[[[<((<[<><>][()[]]><(<><>)>))>{{<(<<>[]>{{}})[[[]<>]({}())]><{{()<>>[[]<>]}[<{}{}>{<>{}}]>}[{<(<
([([(<[{<[[{<{<>[]}>{{{}()]<{}()>}}<([{}()]{{}<>})[([][]){{}<>}]>]{<{{[]{}}{{}<>}}<[[]()]>>[[{()[]}{(){}}]{[
{<{([([{<<<<{[<>()]<[]>}[[()<>]<()>]>>(([[<>[]][{}{}]])((([][]){<><>})([[]{}]<()<>})))><{<<[()()]<[]()>
[{({[{[(([([{{{}<>}{()<>}}(([]<>){{}{}})][<{()}{{}{}}>(<<>()>[<>()])])]))<<<({((<>()){[]{}})[{
([([(<(({<(<<<{}[]>){{<><>}[[]{}]}>[{{[][]}<<><>>}])<{<<[]>(()[])>[[{}()]<[]<>>]}{({[]()}[<><>]){{{}[]}[{
{{[{<{((<((<<<(){}>>{([]{})[[]()]}>([({}{})]{<()>{[]{}}}))[[(<<><>>)]<<<{}{}><(){}>>[({}[])({}
<{[({{<<((([[[(){}][{}<>]]<(<>[])<[]()>>]<[[{}()]({}())]>)({<[(){}]>{(<><>){[]{}}}})){{{<<[]()>[()<>]>[<
(<[[(<((<[[<{[[]()][()<>]}<[[][]]<[][]>>>((({}())((){}))(<{}<>]{()()}))]]>[[{<{[{}<>]}>([[{}<>](()
<<<{<(<[<{[[([<>()][()<>])(<<>()>[{}()])][<{<>()}>]]}<<<({<>[]}([]{}))<<(){}>>>[[({}())(())]]>{({({}[
([<<<{<{({<[{(()<>)<()()>}]<[({}<>)]>>{[[{<>{}}(()[])](<<>>[[]<>])]}}{<<{<<>()>}><{{<>()}<<><>>}{<(){}>[(){
{{(<<[{{({({({[]()}<{}()>)(([][])[()<>])}<{(<>())[()<>]}>)[[(([]<>)[[]<>])]]}[({[({}()){{}>]})
<((((<{{{{{[{[(){}]([][])}[{<>{}}([]<>)]]([((){})]<[[][]][<><>]>)}}<(<{(()<>)([]{})}><([()<>]{<>()
<{<{<(<(<<<(<[[][]]<<>()>><[<>[]][[]]>)[<[<>{}][<>()]>]>{<{(()){{}()}}[<{}<>><<><>>]>[{<{}[]><<><>>}]}>{(
{[{<<(<([({{<<[]<>>[<>{}]>{<{}<>>([]<>)}}([<<>{}>((){})}<{<>[]}>)}<<({{}()})<(<>[])[[]]>>[[<<>[]>{()[]}][[[]
<<<<[<{<[{{(<[<>]<[]{}>><(<>{}){{}()}>)[[{<>{}}{{}[]}](<[]>[<>{}])]}{{[{{}[]}(()<>)]<([]())(
[([({[[{<{{<<{()()}<{}{}>>({{}{}}[{}{}]>>[{(<>{})<()()>}[[<>[]]<{}()>]]}[<<{<><>}(()[])>(<{}[]>
[<<[[(({<[[([(<>[]){()[]}][(<><>)[<>[]]])]<({<{}{}>(()[])}[<{}<>>({}())])((({}{})<{}[]>)[{{}<>}{{}{}}])
(({({[<<[<[([<<><>){[]{}}][<()<>><[]<>>])({[{}<>]<[]<>>}<({}{})[{}[]]>)][{((<><>)(()[]))}[<<{}()>{<>
<((<[(<(<[[([{(){}}<<>()>]({(){}}{(){}}))]][{{[{[][]]{<>{}}]{[{}<>]([]{})}}}[<{[[]{}][<>()]}[(()[])<
{((<<{({<[([(([]())([]()))(<[][]>{()})])<<[<<>[]>[<>())](<()<>><()()>)>>]>{{[{<[<>{}]<[]<>>>}<{{<><>}<
{<<<<[((<{({<{<>[]}{<>()}><{<><>){<>()}>}([[[]()][(){}]]<<()<>>{<><>}>)){[{{<>[]}{[]()}}{(<>())
({<<<<[{<{<{(<{}{}><()[]>)[{<>{}}]}>(<[([]{}){<><>}]{<<><>>[()[]]}}<[{()[]}{()[]}][{{}[]}{[][]}]>)}>}]
({({{<{{{[<{{(<><>)}({[]()}{<><>})}{<[{}[]]<[]<>>>[(<>[]){()()}]}><[[<<>()><[][]>]]>]<<[{[[]()](
<{[<([<[({([{(<>{}){()}}<([]<>)[{}{}]>)[[<()[]><{}<>>][(<>{})[()()]]]){<{({}){{}{}}}<{<>()}[[
{((({[{<{[<({[{}()]({}{})}<(<>)(()())>)({[[]{}](<><>)}[<<>[]>[<>[]]])><<[{[]<>}][([][])<[]()>]>(
({[((([<[(<{[(<>[])(()[])]}<[([][])([]<>)]<(()())>>>((([(){}])<(<>())<<><>>>)<[[()<>>{{}{}
[{{((<{[(<{[{{[][]}{<><>}}[[()[]]<[][]>]]<<({}[])((){})>>}>[(<([[]()]<{}[]>)([{}<>])>({<<>[]>(<>[])}[(
((<((<[<(<[{(<[]()>[()[]])((())(()[]))}{[[{}<>]([]{})]<[[]()]>}]>)><([<[<{[]<>}<{}[]>>[[(){}]]]({[[][]]{
[(([([(([<<(<{<>}{[][]}>)[{[()<>]{{}{}}}({{}{}}<[]()>)]>>{([({<><>}<[]>){<{}{}>[()<>]}]<<[[]{}]{{
[(<{<[[{[<<{<[[]<>]<[]()>>{{[]<>}}}><[[{{}()}([]<>)]][({{}<>}{{}{}})<[[][]](()())>]>><<({([]{})<<>{}>}){
<{[<[(<<[[[[{<{}[]><[]<>>](<{}[]>{()[]})](<[<>()][[][]]>([()()]<<>()>))]]({([<()[]>[{}()]])<{[[]()]}{<[][
<{{{([[([{{{<({}[])>}}<<({<>{}}{{}()))<({}{}){[]{}}>>[[(<>())[{}[]]]<<[]{}>{<>[]}>]>}([{[<<
[{<(({{<[{[[([<>{}]{<>{}})(((){})[{}[]])][{<{}<>>}[([]{})<{}>]]]}{<<([<>{}][()[]})[{{}}<{}()>]>(
[((<[{<<[<[{[{{}()}[{}[]]]<[<>[]][{}<>]>}]>]{[([([[]<>]{{}[]})[<(){}>[()[]]]]<<({}[])<[]()>>[(
[{([<{([(({(<[[]<>]>{({}()){<><>}})([([]())[[]<>]])}(<[({}())(<>())]<{()<>}[[]<>]>>)){{([[<><>][()[]>](<[][]>
<<(<<<{{{<<(<<[]<>>{<>()}>[<[]>])<{<{}<>>}{[{}{}]<<>[]>}>><{<<<>{}>({}<>)>}{([()[]]<<>()>)(<<><>><[]{}>)}>><
{[<<[{{(<<[((({}{})[{}{}])(({}<>)[{}()]))]>{([[[(){}]<{}<>>][[{}[]]{()[]}]](<{[]{}}(<>[]>>))}>)}[(<
<{{[[<[[[(((({<><>}{{}{}})<[<>()]([]())>)[<{{}<>}>{((){})[[][]]}]))<{<{[[]()]<[][]>}{<[]<>>(<>
{<[<<([[[[{{<({}<>)<{}()>>[(<>())({}[])]}<{([][])({}<>)}>}(({[<>{}]{[]{}}}<(<>{})>)[<{[][]}{[][]}>{({}()){
[[({{[(((({<{{<><>]}{(<><>){<><>}}>(<[()<>]<{}{}>>((<><>){<>[]}))}{<[[{}[]]([][])][{{}[]}[
[{{<([((<<{(((<><>)<(){}>))((({}[]){<>()})(<{}()}({}{})))}><[<<{<>[]}[()<>]>{[<>{}]{[]()}}>{{
[<{<{{({{<<<{[<><>]<[][]>}<<(){}>(<>)>>>([<{[]()}{{}[]}>{<{}()><[]<>>}]([([]())[[]]]([[]()]<<>{}>)))>
<[{<[(<{{([[<[{}{}]><([]<>)(()())>][<((){})[[]()]>[([]<>){<><>}]]]{<{<[]<>><<>>}{<{}<>><[]{}
{[((((((({([([(){}]([]<>)){[{}](<>[])}]{[<<>()>([]<>)]<<[][]>{[]<>}>})<<[{{}[]}(<><>)]<[()<>]
([({(([[[([[((<>{}){{}{}}]{[()<>]((){})}]((({})(<>[])){[{}{}]<<>()>})]{({(())[<>{}]}((<>{})
{<[<{(<[{<[{(<{}()>)[<<>[]>(()<>)]}([{()[]}<{}<>>])}(({<[]{}><{}{}>}([[]<>]{{}()})){[[{}<>]
<<({[[<<[([(<[<><>]{<>{}}>{<(){}>(()())})<{[<>{}]<()[]>}>]<{[{<>{}}<<>()>]<{{}()}[()<>]>}<[[{}<>][{
"""

from numpy import median

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    None: 0
}

points2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

matching = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

def parse_input(data):
    return data.strip().splitlines()

def check(line):
    stack = []

    for c in line:
        if c in matching:
            stack.append(c)
        elif c in matching.values():
            if not stack:
                return c
            v = stack.pop()
            if matching[v] != c:
                return c
        else:
            raise ValueError(f"Incorrect character: {c!r}")

def remaining_chars(line):
    stack = []

    for c in line:
        if c in matching:
            stack.append(c)
        elif c in matching.values():
            stack.pop()
    return ''.join(reversed(stack))

def part1(lines, debug=False):
    bad_chars = [check(line) for line in lines]
    if debug:
        print(bad_chars)
    return sum([points[c] for c in bad_chars])

def part2(lines, debug=False):
    good_lines = [line for line in lines if check(line) is None]
    if debug:
        print(good_lines)
    remaining = [remaining_chars(line) for line in good_lines]

    scores = []
    for r in remaining:
        s = 0
        for c in r:
            s *= 5
            s += points2[c]
        scores.append(s)
    if debug:
        print(scores)
    return int(median(scores))

print("Day 10")
print("Part 1")
print("Test input")
test_lines = parse_input(test_input)
test_res = part1(test_lines, debug=True)
print(test_res)

print("Puzzle input")
lines = parse_input(input)
res = part1(lines)
print(res)

print("Part 2")
test_lines = parse_input(test_input)
test_res = part2(test_lines, debug=True)
print(test_res)

print("Test input")
lines = parse_input(input)
res = part2(lines)
print(res)
