blacklist = ['achsenmann', '4chsenmann', 'achs3nmann', 'achsenm4nn', '4chs3nmann', '4chsenm4nn', '4chs3nm4nn',
             'achs3nm4nn',
             'achsenmänner',
             'arsch', '4rsch', '*rsch',
             'Asozialer',
             'asylant', '4sylant', 'asyl4nt', '4syl4nt', '*sylant', 'asyl*nt', '*syl*nt',
             'bastard' 'b4stard', 'bast4rd', 'b4st4rd', 'b*stard', 'bast*rd', 'b*st*rd', 'b4st*rd', 'b*st4rd',
             'behindert', 'b3hindert', 'beh1ndert', 'behind3rt', 'b3h1ndert', 'b3hind3rt', 'b3h1nd3rt', 'b*hindert',
             'beh*ndert', 'behind*rt', 'b*h*ndert', 'b*hind*rt', 'b*h*nd*rt',
             'behinderung', 'b3hinderung', 'beh1nderung', 'behind3rung', 'b3h1nderung', 'b3hind3rung', 'b3h1nd3rung',
             'b*hinderung', 'beh*nderung', 'behind*rung', 'behinder*ng', 'b*h*nderung', 'b*hind*rung', 'b*hinder*ng',
             'b*h*nd*rung', 'b*h*nder*ng', 'b*h*nd*r*ng',
             'bumsen', 'bums3n', 'b*msen', 'bums*n', 'b*ms*n', 'b*ms3n',
             'dumm',
             'fick', 'f1ck', 'f*ck', 'fuck',
             'fotze', 'f0tze', 'fotz3', 'f0tz3', 'f*tze', 'fotz*', 'f*tz3', 'f0tz*',
             'fresse', 'fr3sse', 'fress3', 'fr3ss3', 'fr*sse', 'fress*', 'fr*ss3', 'fr3ss*',
             'hitler', 'h1tler', 'hitl3r', 'h1tl3r', 'h*tler', 'hitl*r', 'h*tl*r', 'h1tl*r', 'h*tl3r',
             'hundesohn', 'hund3sohn', 'hundes0hn', 'hund3s0hn', 'h*ndesohn', 'hund*sohn', 'hundes*hn', 'h*nd*sohn',
             'h*ndes*hn', 'hund*s*hn', 'h*nd*s*hn', 'h*nd3sohn', 'h*ndes0hn', 'h*nd3s0hn', 'hund*s0hn', 'hund3s*hn',
             'hure', 'hur3', 'h*re', 'h*r*', 'h*r3',
             'idiot', '1diot', 'id1ot', 'idi0t', '1d1ot', '1di0t', '1d10t', 'id10t', '*diot', 'id*ot', 'idi*t', '*d*ot',
             '*di*t', '*d**t',
             'nigger', 'n1gger', 'nigg3r', 'n1gg3r', 'n*gger', 'nigg*r', 'n*gg*r', 'n1gg*r', 'n*gg3r',
             'nigga', 'n1gga', 'n1gg4', 'n*gga', 'nigg*', 'n*gg*', 'n1gg*', 'n*gg4',
             'nutte', 'nutt3', 'n*tte', 'nutt*', 'n*tt*', 'n*tt3',
             'schlampe', 'schl4mpe', 'schlamp3', 'schl4mp3', 'schl*mpe', 'schlamp*', 'schl*mp*', 'schl4mp*', 'schl*mp3',
             'stalin', 'st4lin', 'stal1n', 'st4l1n', 'st*lin', 'stal*n', 'st*l*n', 'st4l*n', 'st*l1n',
             'terrorist', 't3rrorist', 'terr0rist', 'terror1st', 't3rr0rist', 't3rror1st', 't3rr0r1st', 't*rrorist',
             'terr*rist', 'terror*st', 't*rr*rist', 't*rror*st', 't*rr*r*st', 't*rr0rist', 't*rror1st', 't*rr0r1st',
             't3rr*rist', 'terr*r1st', 't3rr*r1st', 't3rror*st', 'terr0r*st', 't3rr0r*st', 't3rr*r*st', 't*rr0r*st',
             't*rr*r1st',
             'verpiss', 'v3rpiss', 'verp1ss', 'v3rp1ss', 'v*rpiss', 'verp*ss', 'v*rp*ss' 'v3rp*ss', 'v*rp1ss']


def is_blacklisted(content):
    for word in blacklist:
        if word.lower() in content.lower():
            return True
    return False


def censorer(content):
    for word in blacklist:
        if word.lower() in content.lower():
            content = content.lower().replace(word.lower(), '*' * len(word))
    return content