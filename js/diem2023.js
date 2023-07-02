const axios = require('axios').default;
const cheerio = require('cheerio');

const options = {
  method: 'GET',
  url: 'https://tsdaucap.hanoi.gov.vn/TraCuu/KetQuaTraCuuTuyenSinh10',
  params: {
    key: 'aW5wdXRERIaI5PYKLYXRhPTIweeg0mx4XsMTE2NSSzRjKXCGwZ0eXBlQ2hlY2s9MDI='
  },
  headers: {
    Accept: 'text/html, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    Connection: 'keep-alive',
    Cookie: 'BIGipServerPool_TSDC_HN=1915228332.50719.0000; .AspNetCore.Antiforgery.68HoDSos0ic=CfDJ8CjI4AkC0xlNiBlQXi0796q7YGMIaMZsTi5RxX_GhTNJyU_H3LsN8GdE37fIf8Uar0YNRz_8IZ-IJioWmOD-aqvtqZVlyLnQoHdxas16GFlHVVE6SD7EpFI09Wsb0wLRYQ7HltmPPeK4DaB-QY5UDuw',
    Referer: 'https://tsdaucap.hanoi.gov.vn/tra-cuu-tuyen-sinh-10',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^^"Windows^^"'
  }
};

axios.request(options)
  .then(function (response) {
    const $ = cheerio.load(response.data);
    const boxThongTinDiem = $('.col-md-8.box-thong-tin-diem');
    const rows = boxThongTinDiem.find('.row');

    // Extract the relevant data from the rows
    const soBaoDanh = rows.eq(0).find('b').text();
    const maHocSinh = rows.eq(1).find('b').text();
    const hoTen = rows.eq(2).find('b').text();
    const diemThi = rows.eq(3).find('b').text();

    // Do something with the extracted data
    console.log({
      soBaoDanh,
      maHocSinh,
      hoTen,
      diemThi,
    });
  })
  .catch(function (error) {
    console.error(error);
  });