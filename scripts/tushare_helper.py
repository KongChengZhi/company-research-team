#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tushare Data Helper for Company Research
用于公司研究的Tushare数据辅助脚本
"""

import os
import pandas as pd
import tushare as ts
from datetime import datetime, timedelta

# Initialize Tushare
token = os.getenv('TUSHARE_TOKEN')
pro = None
if token:
    try:
        ts.set_token(token)
        pro = ts.pro_api(token)
        print("Tushare 初始化成功")
    except Exception as e:
        print(f"Tushare 初始化失败: {e}")
else:
    print("未设置 TUSHARE_TOKEN 环境变量，Tushare功能已禁用")


def get_stock_code(stock_name: str) -> str:
    """将股票名称转换为Tushare格式 (如: 000001.SZ)"""
    if not pro:
        return None
    try:
        df = pro.stock_basic(ts_name=stock_name, fields='ts_code,symbol,name')
        if df is not None and len(df) > 0:
            return df.iloc[0]['ts_code']
    except Exception as e:
        print(f"获取股票代码失败: {e}")
    return None


def get_company_info(ts_code: str) -> pd.DataFrame:
    """获取公司基本信息"""
    if not pro:
        return None
    try:
        return pro.stock_basic(ts_code=ts_code, fields='ts_code,symbol,name,area,industry,list_date,delist_date')
    except Exception as e:
        print(f"获取公司信息失败: {e}")
        return None


def get_daily_price(ts_code: str, start_date: str = None, end_date: str = None) -> pd.DataFrame:
    """获取每日行情数据"""
    if not pro:
        return None
    if not start_date:
        start_date = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')
    if not end_date:
        end_date = datetime.now().strftime('%Y%m%d')
    try:
        return pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
    except Exception as e:
        print(f"获取行情数据失败: {e}")
        return None


def get_daily_indicators(ts_code: str, start_date: str = None, end_date: str = None) -> pd.DataFrame:
    """获取每日财务指标 (PE, PB, 换手率等)"""
    if not pro:
        return None
    if not start_date:
        start_date = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')
    if not end_date:
        end_date = datetime.now().strftime('%Y%m%d')
    try:
        return pro.daily_basic(ts_code=ts_code, start_date=start_date, end_date=end_date,
                              fields='ts_code,trade_date,pe,pb,turnover_rate,volume_ratio,float_mv,total_mv')
    except Exception as e:
        print(f"获取每日指标失败: {e}")
        return None


def get_income_statement(ts_code: str, year: int = None) -> pd.DataFrame:
    """获取利润表"""
    if not pro:
        return None
    if not year:
        year = datetime.now().year
    try:
        return pro.income(ts_code=ts_code, start_date=f'{year}0101', end_date=f'{year}1231',
                         fields='ts_code,report_date,revenue,profit,total_profit,eps')
    except Exception as e:
        print(f"获取利润表失败: {e}")
        return None


def get_balance_sheet(ts_code: str, year: int = None) -> pd.DataFrame:
    """获取资产负债表"""
    if not pro:
        return None
    if not year:
        year = datetime.now().year
    try:
        return pro.balancesheet(ts_code=ts_code, start_date=f'{year}0101', end_date=f'{year}1231',
                              fields='ts_code,report_date,total_assets,total_liab,total_hldr_eqy')
    except Exception as e:
        print(f"获取资产负债表失败: {e}")
        return None


def get_cashflow_statement(ts_code: str, year: int = None) -> pd.DataFrame:
    """获取现金流量表"""
    if not pro:
        return None
    if not year:
        year = datetime.now().year
    try:
        return pro.cashflow(ts_code=ts_code, start_date=f'{year}0101', end_date=f'{year}1231',
                          fields='ts_code,report_date,op_cashflow,inv_cashflow,finc_cashflow')
    except Exception as e:
        print(f"获取现金流量表失败: {e}")
        return None


def get_financial_indicators(ts_code: str, start_year: int = None) -> pd.DataFrame:
    """获取财务指标 (ROE, ROA, 毛利率等)"""
    if not pro:
        return None
    if not start_year:
        start_year = datetime.now().year - 3
    try:
        return pro.fina_indicator(ts_code=ts_code, start_date=f'{start_year}0101',
                                 fields='ts_code,report_date,roe,roa,gross_margin,net_profit_margin,debt_to_asset')
    except Exception as e:
        print(f"获取财务指标失败: {e}")
        return None


def get_margin_trading(ts_code: str, start_date: str = None, end_date: str = None) -> pd.DataFrame:
    """获取融资融券数据"""
    if not pro:
        return None
    if not start_date:
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y%m%d')
    if not end_date:
        end_date = datetime.now().strftime('%Y%m%d')
    try:
        return pro.margin(ts_code=ts_code, start_date=start_date, end_date=end_date,
                         fields='ts_code,trade_date,margin_balance,secu_balance,margin_ratio')
    except Exception as e:
        print(f"获取融资融券数据失败: {e}")
        return None


def get_money_flow(ts_code: str, start_date: str = None, end_date: str = None) -> pd.DataFrame:
    """获取资金流向数据"""
    if not pro:
        return None
    if not start_date:
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y%m%d')
    if not end_date:
        end_date = datetime.now().strftime('%Y%m%d')
    try:
        return pro.moneyflow(ts_code=ts_code, start_date=start_date, end_date=end_date,
                            fields='ts_code,trade_date,main_net_inflows,large_net_inflows,medium_net_inflows,small_net_inflows')
    except Exception as e:
        print(f"获取资金流向失败: {e}")
        return None


def get_top10_shareholders(ts_code: str, year: int = None) -> pd.DataFrame:
    """获取前十大股东"""
    if not pro:
        return None
    if not year:
        year = datetime.now().year
    try:
        return pro.top10_holders(ts_code=ts_code, start_date=f'{year}0101', end_date=f'{year}1231',
                                fields='ts_code,end_date,holder_name,hold_ratio')
    except Exception as e:
        print(f"获取前十大股东失败: {e}")
        return None


def get_management_info(ts_code: str) -> pd.DataFrame:
    """获取管理层信息"""
    if not pro:
        return None
    try:
        return pro.stk_managers(ts_code=ts_code,
                               fields='ts_code,end_date,name,gender,birth_year,edu,nationality,position,resume')
    except Exception as e:
        print(f"获取管理层信息失败: {e}")
        return None


def get_dividend_history(ts_code: str) -> pd.DataFrame:
    """获取分红历史"""
    if not pro:
        return None
    try:
        return pro.dividend(ts_code=ts_code, fields='ts_code,end_date,cash_div,stock_div,bonus_share')
    except Exception as e:
        print(f"获取分红历史失败: {e}")
        return None


# 宏观经济数据
def get_gdp_data() -> pd.DataFrame:
    """获取GDP数据"""
    if not pro:
        return None
    try:
        return pro.cn_gdp()
    except Exception as e:
        print(f"获取GDP数据失败: {e}")
        return None


def get_cpi_data() -> pd.DataFrame:
    """获取CPI数据"""
    if not pro:
        return None
    try:
        return pro.cn_cpi()
    except Exception as e:
        print(f"获取CPI数据失败: {e}")
        return None


def get_pmi_data() -> pd.DataFrame:
    """获取PMI数据"""
    if not pro:
        return None
    try:
        return pro.cn_pmi()
    except Exception as e:
        print(f"获取PMI数据失败: {e}")
        return None


def get_shibor_data() -> pd.DataFrame:
    """获取SHIBOR数据"""
    if not pro:
        return None
    try:
        return pro.shibor()
    except Exception as e:
        print(f"获取SHIBOR数据失败: {e}")
        return None


def get_lpr_data() -> pd.DataFrame:
    """获取LPR数据"""
    if not pro:
        return None
    try:
        return pro.shibor_lpr()
    except Exception as e:
        print(f"获取LPR数据失败: {e}")
        return None


def get_money_supply() -> pd.DataFrame:
    """获取货币供应量M1/M2数据"""
    if not pro:
        return None
    try:
        return pro.cn_m()
    except Exception as e:
        print(f"获取货币供应量失败: {e}")
        return None


def get_industry_classification() -> pd.DataFrame:
    """获取申万行业分类"""
    if not pro:
        return None
    try:
        return pro.index_classify()
    except Exception as e:
        print(f"获取行业分类失败: {e}")
        return None


def get_index_daily(ts_code: str = '000300.SH', start_date: str = None, end_date: str = None) -> pd.DataFrame:
    """获取指数日线数据"""
    if not pro:
        return None
    if not start_date:
        start_date = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')
    if not end_date:
        end_date = datetime.now().strftime('%Y%m%d')
    try:
        return pro.index_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
    except Exception as e:
        print(f"获取指数日线失败: {e}")
        return None


if __name__ == '__main__':
    # 使用示例
    print("Tushare 公司研究数据辅助工具")
    print("=" * 50)

    if pro:
        # 示例: 获取平安银行数据
        ts_code = '000001.SZ'
        print(f"\n获取 {ts_code} 的数据...")

        info = get_company_info(ts_code)
        if info is not None:
            print(f"公司名称: {info.iloc[0]['name']}")
            print(f"所属行业: {info.iloc[0]['industry']}")

        daily = get_daily_price(ts_code, start_date='20240101')
        if daily is not None:
            print(f"最新收盘价: {daily.iloc[-1]['close']}")

        indicators = get_daily_indicators(ts_code)
        if indicators is not None:
            print(f"最新PE: {indicators.iloc[-1]['pe']}")
    else:
        print("\n请设置 TUSHARE_TOKEN 环境变量以启用Tushare功能")
        print("例如: export TUSHARE_TOKEN=your_token")
