def cladata(li, le):
    live = ["人力类", "业务管理类", "IT类", "IT类-规划与需求分析序列", "IT类-系统运维序列", "IT类-研发序列",\
            "IT类-基础架构序列", "综合类", "广告类", "战略类", "法律类", "财务类", "综合类2"]
    leve = ["中级", "高级", "资深", "专家"]
    return "[%s-%s]" % (live[li], leve[le])


if __name__ == '__main__':
    print(cladata(0, 1))
