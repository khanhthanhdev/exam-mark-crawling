import fetch from "node-fetch";
import { parse } from "node-html-parser";

export const getToken = async (id, type = "01") => {
  try {
    const res = await fetch(
      "https://tsdaucap.hanoi.gov.vn/tra-cuu-diem-thi-10",
      {
        headers: {
          "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
          requestverificationtoken:
            "CfDJ8CjI4AkC0xlNiBlQXi0796pPe6spT-DfbWy4y6fzzNzKn6gTNWqRaiTYsB6cq9mcBCvG0RDSZF5_7eeno9ZwSU8bYYF4FaC2fPNPde5hishfnDuriO0mixSjHM1D3jKiFIKD0PCx9zTEJ_BkdfjdnGg",
          cookie:
            "BIGipServerPool_TSDC_HN=1915228332.34048.0000; .AspNetCore.Antiforgery.68HoDSos0ic=CfDJ8CjI4AkC0xlNiBlQXi0796pPe6spT-DfbWy4y6fzzNzKn6gTNWqRaiTYsB6cq9mcBCvG0RDSZF5_7eeno9ZwSU8bYYF4FaC2fPNPde5hishfnDuriO0mixSjHM1D3jKiFIKD0PCx9zTEJ_BkdfjdnGg",
        },
        body: `LOAI_TRA_CUU=${type}&GIA_TRI=${id}&CaptchaTime=CfDJ8GaVrXyqbnxOu3wE-OMJ5pjGk_ehkKnj_M_GmN6fsxxJf7y7LQEg8XabVJ6jclU6LhH7r1xhVcwmMkxb395cMgGVKpnQLhN7LOsoEjeVCPPXWY9IUJ6Nd80ey-PnqgRK9A&CaptchaInput=UN61`,
        method: "POST",
      }
    );

    const data = await res.json();

    return data.key;
  } catch (error) {
    return null;
  }
};

export const getMarkFromToken = async (token) => {
  try {
    const source = await (
      await fetch(
        `https://tsdaucap.hanoi.gov.vn/TraCuu/KetQuaTraCuuTuyenSinh10?key=${token}`
      )
    ).text();

    const dom = parse(source);

    const mark = dom
      .querySelectorAll(".box-thong-tin-diem .row")[3]
      .querySelector("b").innerText;

    const name = dom
      .querySelectorAll(".box-thong-tin-diem .row")[2]
      .querySelector("b").innerText;

    return {
      name,
      mark,
    };
  } catch (error) {
    const source = await (
      await fetch(
        `https://tsdaucap.hanoi.gov.vn/TraCuu/KetQuaTraCuuTuyenSinh10?key=${token}`
      )
    ).text();

    const dom = parse(source);

    const mark = dom
      .querySelectorAll(".box-thong-tin-diem .row")[3]
      .querySelector("b").innerText;

    const name = dom
      .querySelectorAll(".box-thong-tin-diem .row")[2]
      .querySelector("b").innerText;

    return {
      name,
      mark,
    };
  }
};
