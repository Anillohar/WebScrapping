def address(company_address):
    c_address = str(company_address)
    c_address = c_address.strip('[ < span class ="cont_fl_addr" >')
    c_address = c_address.strip('</span>]')
    return c_address


def name(company_name):
    cname = str(company_name)
    cname = cname.strip('[<span class="lng_cont_name">')
    cname = cname.strip('</span>]')
    return cname
